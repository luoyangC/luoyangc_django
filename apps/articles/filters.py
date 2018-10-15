"""
  Created by Amor on 2018-10-07
"""
import django_filters
from .models import Article

__author__ = '骆杨'


class ArticleFilter(django_filters.rest_framework.FilterSet):
    """
    文章的过滤器
    """
    category = django_filters.NumberFilter(field_name='category', lookup_expr='exact')
    search = django_filters.CharFilter(field_name='title', lookup_expr='icontains')
    tag = django_filters.CharFilter(field_name='tags', lookup_expr='icontains')
    time = django_filters.CharFilter(method='time_filter')
    is_banner = django_filters.BooleanFilter(field_name='is_banner', lookup_expr='exact')

    def time_filter(self, queryset, name, value):
        year, month = value.split('-')
        queryset = queryset.filter(update_time__year=year).filter(update_time__month=month)
        return queryset

    class Meta:
        model = Article
        fields = ['category', 'time', 'search', 'is_banner', 'tag']
