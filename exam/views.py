from django.shortcuts import render
from django.views.generic import TemplateView


# Create your views here.
class IndexView(TemplateView):
    template_name = 'exam/index.html'

    def get_context_data(self,**kwargs):
        context = super().get_context_data(**kwargs)
        context["message"] = '自然数nに対して，次のように再帰的に定義される関数f(n)を考える。f(5)の値はどれか。\nf(n)：if n≦1 then return 1 else return n＋f(n−1)'
        return context