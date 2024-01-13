# import the render function from the django.shortcuts module.
from django.shortcuts import render

# Create courses list.
courses_list = [{
    'name':
    'Інформаційні технології',
    'desc':
    'Курс для тих, хто цікавиться розробкою програмного забезпечення, створенням веб-сайтів та мобільних додатків.',
    'disciplines': [{
        'name': 'Основи програмування',
        'teacher': 'Іванов І. І.'
    }, {
        'name': 'Бази даних',
        'teacher': 'Петров П. П.'
    }, {
        'name': 'Веб-розробка',
        'teacher': 'Сидорова О. М.'
    }]
}, {
    'name':
    'Електронні системи',
    'desc':
    'Курс для тих, хто хоче вивчити теорію та практику в галузі проектування та експлуатації електронних систем.',
    'disciplines': [{
        'name': 'Мікропроцесорна техніка',
        'teacher': 'Шевченко Т. С.'
    }, {
        'name': 'Електронні пристрої',
        'teacher': 'Ковальов А. П.'
    }, {
        'name': 'Схемотехніка',
        'teacher': 'Семенов Д. О.'
    }]
}, {
    'name':
    'Мехатроніка',
    'desc':
    'Курс для тих, хто хоче навчитися створювати мехатронні системи, які поєднують електронні компоненти з механічними.',
    'disciplines': [{
        'name': 'Механіка',
        'teacher': 'Козлов С. В.'
    }, {
        'name': 'Електротехніка',
        'teacher': 'Шевчук О. І.'
    }, {
        'name': 'Керування мехатронними системами',
        'teacher': 'Гриньов М. В.'
    }]
}, {
    'name':
    'Автоматика та приладобудування',
    'desc':
    'Курс для тих, хто цікавиться розробкою та застосуванням автоматичних систем керування та приладів.',
    'disciplines': [{
        'name': 'Програмування мікроконтролерів',
        'teacher': 'Козлов О. О.'
    }, {
        'name': 'Автоматичне керування',
        'teacher': 'Шевчук М. О.'
    }, {
        'name': 'Системи приладів',
        'teacher': 'Сидоренко М. В.'
    }]
}, {
    'name':
    'Безпека інформаційних технологій',
    'desc':
    'Курс для тих, хто цікавиться захистом інформації від несанкціонованого доступу, кібератак та інших загроз.',
    'disciplines': [{
        'name': 'Криптографія',
        'teacher': 'Семенов С. В.'
    }, {
        'name': 'Безпека мереж',
        'teacher': 'Ковальова І. І.'
    }, {
        'name': 'Антивірусна захист',
        'teacher': 'Богданов М. В.'
    }]
}, {
    'name':
    'Електроенергетика',
    'desc':
    'Курс для тих, хто цікавиться виробництвом, передачею та розподілом електроенергії.',
    'disciplines': [{
        'name': 'Промислова електроніка',
        'teacher': 'Савченко С. В.'
    }, {
        'name': 'Енергетичні системи',
        'teacher': 'Гаврилюк О. І.'
    }, {
        'name': 'Енергетична ефективність',
        'teacher': 'Корнієнко М. В.'
    }]
}]

# Create costs list
costs_list = [{
    'name': 'Інформаційні технології',
    'cost': '15 000 грн'
}, {
    'name': 'Електронні системи',
    'cost': '12 000 грн'
}, {
    'name': 'Мехатроніка',
    'cost': '14 000 грн'
}, {
    'name': 'Автоматика та приладобудування',
    'cost': '11 000 грн'
}, {
    'name': 'Безпека інформаційних технологій',
    'cost': '18 000 грн'
}, {
    'name': 'Електроенергетика',
    'cost': '13 000 грн'
}]


def home(request):
    # Render the main homepage of the website.
    return render(request, 'techcoll/main.html')


def courses(request):
    # Render the courses page of the website.
    return render(request, 'techcoll/courses.html', {'courses': courses_list})


def costs(request):
    # Render the costs page of the website.
    return render(request, 'techcoll/costs.html', {'costs': costs_list})


def contact(request):
    # Render the contact page of the website.
    return render(request, 'techcoll/contact.html')
