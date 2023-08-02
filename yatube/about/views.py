from django.views.generic.base import TemplateView


class AboutAuthorView(TemplateView):
    template_name = 'about/author.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        context['author_title'] = 'Привет, я Александр Ершов создатель сервиса'
        context['author_text'] = ('Готов в открытым предложениям - писать в telegram @soyage')

        return context


class AboutTechView(TemplateView):
    template_name = 'about/tech.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        context['tech_title'] = 'Технологии'
        context['tech_text'] = 'Python — современный язык, разработка на нем быстрая и качественная. Используют его для средних и больших проектов. Программистов найти проблематично, и стоят они не дешево. ' \
                               'Django — свободный фреймворк для веб-приложений на языке Python, использующий шаблон проектирования MVC. Проект поддерживается организацией Django Software ' \
                               'Bootstrap — это бесплатный CSS-фреймворк с открытым исходным кодом, предназначенный для адаптивной, ориентированной на мобильные устройства фронтальной веб-разработки. '
        context['tech_technologies_list'] = ('Python', 'Django', 'Bootstrap')

        return context
