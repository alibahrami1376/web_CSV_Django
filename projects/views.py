import logging
from django.shortcuts import render, get_object_or_404
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
from django.db.models import Q, Count
from projects.models import Projects, Category
from django.http import HttpRequest

logger = logging.getLogger(__name__)

def projects_list(request: HttpRequest, category_slug=None):
    """نمایش لیست تمام پروژه‌ها"""
    logger.info(f'Projects list accessed with category_slug: {category_slug}')
    try:
        projects = Projects.objects.all()
        logger.info(f'Total projects found: {projects.count()}')
        
        # فیلتر بر اساس دسته‌بندی (از URL یا GET parameter)
        if category_slug:
            logger.info(f'Filtering by category slug: {category_slug}')
            projects = projects.filter(category__slug=category_slug)
        else:
            category_slug = request.GET.get('category')
            if category_slug:
                logger.info(f'Filtering by category from GET: {category_slug}')
                projects = projects.filter(category__slug=category_slug)
        
        # فیلتر پروژه‌های ویژه
        featured_only = request.GET.get('featured')
        if featured_only == 'true':
            logger.info('Filtering featured projects only')
            projects = projects.filter(featured=True)
        
        # جستجو
        search_query = request.GET.get('search', '').strip()
        if search_query:
            logger.info(f'Searching for: {search_query}')
            projects = projects.filter(
                Q(title__icontains=search_query) |
                Q(description__icontains=search_query) |
                Q(content__icontains=search_query)
            )
            logger.info(f'Projects after search: {projects.count()}')
        
        # فیلتر بر اساس وضعیت
        status_filter = request.GET.get('status')
        if status_filter:
            logger.info(f'Filtering by status: {status_filter}')
            projects = projects.filter(status=status_filter)
        
        # مرتب‌سازی
        sort_options = {
            'newest': '-created_date',
            'oldest': 'created_date',
            'most_viewed': '-view_count',
            'title_asc': 'title',
            'title_desc': '-title',
        }
        sort_by = request.GET.get('sort', 'newest')
        sort_field = sort_options.get(sort_by, '-created_date')
        logger.info(f'Sorting by: {sort_by} ({sort_field})')
        projects = projects.order_by(sort_field)
        
        # Pagination
        paginator = Paginator(projects, 9)  # 9 پروژه در هر صفحه
        page = request.GET.get('page')
        try:
            projects = paginator.page(page)
            logger.info(f'Rendering page {page}')
        except PageNotAnInteger:
            logger.info('Invalid page number, using page 1')
            projects = paginator.page(1)
        except EmptyPage:
            logger.info('Empty page requested, using last page')
            projects = paginator.page(paginator.num_pages)
        
        # دریافت دسته‌بندی‌ها با تعداد پروژه‌ها
        categories = Category.objects.annotate(
            project_count=Count('projects')
        ).order_by('name')
        logger.info(f'Found {categories.count()} categories')
        
        # آمار کلی
        total_projects = Projects.objects.count()
        completed_projects = Projects.objects.filter(status='completed').count()
        in_progress_projects = Projects.objects.filter(status='in_progress').count()
        logger.info(f'Stats - Total: {total_projects}, Completed: {completed_projects}, In Progress: {in_progress_projects}')
        
        context = {
            'projects': projects,
            'categories': categories,
            'current_category': category_slug,
            'current_status': status_filter,
            'search_query': search_query,
            'sort_by': sort_by,
            'page_range': paginator.page_range,
            'total_projects': total_projects,
            'completed_projects': completed_projects,
            'in_progress_projects': in_progress_projects,
        }
        logger.info('Projects list rendered successfully!')
        logger.info('Everything is OK!')
        return render(request, 'projects/projects_list.html', context)
    except Exception as e:
        logger.error(f'Error in projects_list view: {e}')
        raise

def project_detail(request: HttpRequest, project_slug: str = None, project_id: int = None):
    """نمایش جزئیات یک پروژه"""
    logger.info(f'Project detail accessed - slug: {project_slug}, id: {project_id}')
    try:
        # پشتیبانی از هر دو slug و id
        if project_slug:
            project = get_object_or_404(Projects, slug=project_slug)
            logger.info(f'Project found by slug: {project.title}')
        elif project_id:
            project = get_object_or_404(Projects, id=project_id)
            logger.info(f'Project found by id: {project.title}')
        else:
            from django.http import Http404
            logger.error('Project not found: neither slug nor id provided')
            raise Http404("Project not found")
        
        # افزایش تعداد بازدید (فقط یک بار در هر session)
        session_key = f'project_viewed_{project.id}'
        if not request.session.get(session_key, False):
            project.view_count += 1
            project.save(update_fields=['view_count'])
            request.session[session_key] = True
            logger.info(f'View count updated for project {project.id}: {project.view_count}')
        else:
            logger.info(f'Project {project.id} already viewed in this session')
        
        # دریافت پروژه‌های مرتبط (از همان دسته‌بندی)
        related_projects = Projects.objects.filter(
            category__in=project.category.all()
        ).exclude(id=project.id).distinct()[:3]
        logger.info(f'Found {related_projects.count()} related projects by category')
        
        # اگر پروژه مرتبطی نبود، آخرین پروژه‌ها را نشان بده
        if not related_projects.exists():
            related_projects = Projects.objects.exclude(id=project.id).order_by('-created_date')[:3]
            logger.info('No related projects by category, using latest projects')
        
        # دریافت پروژه‌های ویژه
        featured_projects = Projects.objects.filter(featured=True).exclude(id=project.id)[:3]
        logger.info(f'Found {featured_projects.count()} featured projects')
        
        context = {
            'project': project,
            'related_projects': related_projects,
            'featured_projects': featured_projects,
        }
        logger.info('Project detail rendered successfully!')
        logger.info('Everything is OK!')
        return render(request, 'projects/project_detail.html', context)
    except Exception as e:
        logger.error(f'Error in project_detail view: {e}')
        raise