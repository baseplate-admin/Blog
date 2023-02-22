Title: How I fixed `htmx` `redeclaration of let <element>` with `hx-boost=true`
Date: 2023-2-22

# Background :

`htmx` is gaining popularity in `django` ecosystem. For example, I have created my latest [project](https://github.com/baseplate-admin/CoreProject/) with `django` + `htmx`. The sites user page was previously written using [`svelte`](https://github.com/baseplate-admin/CoreProject/tree/dbe619fe24f786042a23d77a7025fcf28bdc5242/frontend/User) but I was not using `django` to it's full capability. ( `django templating language` is such a blessing | I dont even have to deal with tokens and refresh and all other nonsenses )

Thats when I started rewriting `user` from `svelte` to `django` + `django_cripsy_forms`

# The problem :

When I was writing the user code in django I planned to do realtime lookup of username availablity. So thats what I did.

Heres the django code :

```jinja2
{% extends 'user/base.html' %}
<!--prettier-ignore-->
{% block title %} Sign Up {% endblock title %}
<!--prettier-ignore-->
{% load crispy_forms_tags static %}


{% block form %}

<form method="post" action="{% url 'signup_view' %}">
    <div class="flex justify-center mb-10">
        <div class="font-bold text-4xl select-none flex">
            <span class="inline-flex text-white">c</span>
            <span class="inline-flex text-warning">o</span>
            <span class="inline-flex text-white">r</span>
            <span class="inline-flex text-white">e</span>
            &nbsp;
            <span class="inline-flex text-info">p</span>
            <span class="inline-flex text-info">r</span>
            <span class="inline-flex text-info">o</span>
            <span class="inline-flex text-info">j</span>
            <span class="inline-flex text-info">e</span>
            <span class="inline-flex text-info">c</span>
            <span class="inline-flex text-info">t</span>
        </div>
    </div>
    <div class="grid gap-6">
        {% crispy form %}
        <div class="flex justify-center items-center gap-2">
            <button
                class="btn btn-secondary font-bold text-black"
                type="submit"
            >
                Register
            </button>
            or
            <a class="underline" href="{% url 'login_view' %}" hx-boost="true"
                >login</a
            >
        </div>
    </div>
</form>

<!--This is the problem code block-->

<script>
    let el = document.querySelector('#id_username');

    el.addEventListener('input', async () => {});
</script>

{% endblock %}
```

Soon enough I was running into this error.

```typescript
Uncaught SyntaxError: redeclaration of let el
    <anonymous> http://127.0.0.1:8000/user/login/ line 1 > injectedScript:1
    ct http://127.0.0.1:8000/static/js/htmx/htmx.min.js:1
    ht http://127.0.0.1:8000/static/js/htmx/htmx.min.js:1
    Y http://127.0.0.1:8000/static/js/htmx/htmx.min.js:1
    ht http://127.0.0.1:8000/static/js/htmx/htmx.min.js:1
    ue http://127.0.0.1:8000/static/js/htmx/htmx.min.js:1
    o http://127.0.0.1:8000/static/js/htmx/htmx.min.js:1
    Y http://127.0.0.1:8000/static/js/htmx/htmx.min.js:1
    o http://127.0.0.1:8000/static/js/htmx/htmx.min.js:1
    setTimeout handler*o http://127.0.0.1:8000/static/js/htmx/htmx.min.js:1
    fr http://127.0.0.1:8000/static/js/htmx/htmx.min.js:1
    onload http://127.0.0.1:8000/static/js/htmx/htmx.min.js:1
    lr http://127.0.0.1:8000/static/js/htmx/htmx.min.js:1
    Ue http://127.0.0.1:8000/static/js/htmx/htmx.min.js:1
    I http://127.0.0.1:8000/static/js/htmx/htmx.min.js:1
    ze http://127.0.0.1:8000/static/js/htmx/htmx.min.js:1
    Y http://127.0.0.1:8000/static/js/htmx/htmx.min.js:1
    ze http://127.0.0.1:8000/static/js/htmx/htmx.min.js:1
    Ue http://127.0.0.1:8000/static/js/htmx/htmx.min.js:1
    Ue http://127.0.0.1:8000/static/js/htmx/htmx.min.js:1
    pt http://127.0.0.1:8000/static/js/htmx/htmx.min.js:1
    mt http://127.0.0.1:8000/static/js/htmx/htmx.min.js:1
    Y http://127.0.0.1:8000/static/js/htmx/htmx.min.js:1
    mt http://127.0.0.1:8000/static/js/htmx/htmx.min.js:1
    ue http://127.0.0.1:8000/static/js/htmx/htmx.min.js:1
    o http://127.0.0.1:8000/static/js/htmx/htmx.min.js:1
    Y http://127.0.0.1:8000/static/js/htmx/htmx.min.js:1
    o http://127.0.0.1:8000/static/js/htmx/htmx.min.js:1
    setTimeout handler*o http://127.0.0.1:8000/static/js/htmx/htmx.min.js:1
    fr http://127.0.0.1:8000/static/js/htmx/htmx.min.js:1
    onload http://127.0.0.1:8000/static/js/htmx/htmx.min.js:1
    lr http://127.0.0.1:8000/static/js/htmx/htmx.min.js:1
    Ue http://127.0.0.1:8000/static/js/htmx/htmx.min.js:1
    I http://127.0.0.1:8000/static/js/htmx/htmx.min.js:1
    ze http://127.0.0.1:8000/static/js/htmx/htmx.min.js:1
    Y http://127.0.0.1:8000/static/js/htmx/htmx.min.js:1
    ze http://127.0.0.1:8000/static/js/htmx/htmx.min.js:1
    Ue http://127.0.0.1:8000/static/js/htmx/htmx.min.js:1
    Ue http://127.0.0.1:8000/static/js/htmx/htmx.min.js:1
    pt http://127.0.0.1:8000/static/js/htmx/htmx.min.js:1
    mt http://127.0.0.1:8000/static/js/htmx/htmx.min.js:1
    Y http://127.0.0.1:8000/static/js/htmx/htmx.min.js:1
    mt http://127.0.0.1:8000/static/js/htmx/htmx.min.js:1
    ue http://127.0.0.1:8000/static/js/htmx/htmx.min.js:1
    o http://127.0.0.1:8000/static/js/htmx/htmx.min.js:1
    Y http://127.0.0.1:8000/static/js/htmx/htmx.min.js:1
    o http://127.0.0.1:8000/static/js/htmx/htmx.min.js:1
    setTimeout handler*o http://127.0.0.1:8000/static/js/htmx/htmx.min.js:1
    fr http://127.0.0.1:8000/static/js/htmx/htmx.min.js:1
    onload http://127.0.0.1:8000/static/js/htmx/htmx.min.js:1
    lr http://127.0.0.1:8000/static/js/htmx/htmx.min.js:1
    Ue http://127.0.0.1:8000/static/js/htmx/htmx.min.js:1
    I http://127.0.0.1:8000/static/js/htmx/htmx.min.js:1
    ze http://127.0.0.1:8000/static/js/htmx/htmx.min.js:1
    Y http://127.0.0.1:8000/static/js/htmx/htmx.min.js:1
    ze http://127.0.0.1:8000/static/js/htmx/htmx.min.js:1
    Ue http://127.0.0.1:8000/static/js/htmx/htmx.min.js:1
    Ue http://127.0.0.1:8000/static/js/htmx/htmx.min.js:1
    pt http://127.0.0.1:8000/static/js/htmx/htmx.min.js:1
    mt http://127.0.0.1:8000/static/js/htmx/htmx.min.js:1
    Y http://127.0.0.1:8000/static/js/htmx/htmx.min.js:1
    mt http://127.0.0.1:8000/static/js/htmx/htmx.min.js:1
    <anonymous> http://127.0.0.1:8000/static/js/htmx/htmx.min.js:1
    pr http://127.0.0.1:8000/static/js/htmx/htmx.min.js:1
    <anonymous> http://127.0.0.1:8000/static/js/htmx/htmx.min.js:1
    <anonymous> http://127.0.0.1:8000/static/js/htmx/htmx.min.js:1
    <anonymous> http://127.0.0.1:8000/static/js/htmx/htmx.min.js:1
    <anonymous> http://127.0.0.1:8000/static/js/htmx/htmx.min.js:1
line 1 > injectedScript:1:1
```

This was something I never ran into before. As `HTMX` was quite new I didn't find much resource on this weird error. I asked on their [discord channel](https://discord.com/channels/725789699527933952/864934037381971988/1077471927989440574) about this particular error ( this wasn't that uncommon as another user reported this error on their discord [thread](https://discord.com/channels/725789699527933952/1066354856643809400/1066354859001008229) ). But I didn't find any response. Do I started digging deeper into this mess.

At a glance nothing seemed wrong ( I wrote couple project in `react`, `svelte` | So I had a good understanding of JS ).. Maybe because I was not familiar with `django` and `html` I thought. I have never stumbled upon this error in my life before.

# Digging deeper :

So after a while I thought of removing `htmx` and just doing things the plain `django` way. Things started to work nicely again. So was it related to `htmx` afterall? `htmx` for those of you dont know does things in a particular way.

1. It fetches the anchor tags `html`.
2. Replaces `body` with said `html`.
3. Re executes `scripts` inside those `body` tags.

So naturally I thought of disabling execution of `script` tags by moving the scripts to the `head`. It worked :D.

But according to htmx author. After `2.0` release `htmx` would re execute the scripts on the head. At the time of writing there is [`head-support`](https://htmx.org/extensions/head-support/) extension that enables said functionality and it was to be merged into htmx by `2.0` release.

# The Solution :

So I was out of hope at this point. Then I stumbled upon this [stackoverflow thread](https://stackoverflow.com/a/13626288) ( god bless stackoverflow ). Here I learned about scoping functions. I was familiar with function scoping back in my `react` days as `react` didn't support top level await codes and I had to do something like this :

```typescript
(async () => {
    await fetch('');
})();
```

So I modified my code like this :

```typescript
(() => {
    let el = document.querySelector('#id_username');
})();
```

and the error was fixed. ( MAGICALLY!! )

<center>
    ![Alt Text](https://i.giphy.com/media/9r75ILTJtiDACKOKoY/giphy.webp)
</center>

# Moving forward :

If you see the pages source. You can see that the site feels like an SPA ( Single Page Application ) even though its a static site. Thats because the site is using a small `JavaScript` library called `flamethower-router` ( for those of you who follow `fireship.io` you guys should know what this is ).

But I ran into the exact same error that I faced with `htmx` ( maybe its the issue with these frontend routers ).

So I modified the theme's [original script](https://github.com/aleylara/Papyrus/blob/a38df10b27367b5f5fe6c477f7b7ccdb772fa1e9/templates/base.html#L216-L245) to be block scoped.

```typescript
(() => {
    let themeToggleDarkIcon = document.getElementById('theme-toggle-dark-icon');
    let themeToggleLightIcon = document.getElementById(
        'theme-toggle-light-icon'
    );
    if (
        localStorage.getItem('color-theme') === 'dark' ||
        (!('color-theme' in localStorage) &&
            window.matchMedia('(prefers-color-scheme: dark)').matches)
    ) {
        themeToggleLightIcon.classList.remove('hidden');
    } else {
        themeToggleDarkIcon.classList.remove('hidden');
    }
    let themeToggleBtn = document.getElementById('theme-toggle');
    themeToggleBtn.addEventListener('click', function () {
        themeToggleDarkIcon.classList.toggle('hidden');
        themeToggleLightIcon.classList.toggle('hidden');
        if (localStorage.getItem('color-theme')) {
            if (localStorage.getItem('color-theme') === 'light') {
                document.documentElement.classList.add('dark');
                localStorage.setItem('color-theme', 'dark');
            } else {
                document.documentElement.classList.remove('dark');
                localStorage.setItem('color-theme', 'light');
            }
        } else {
            if (document.documentElement.classList.contains('dark')) {
                document.documentElement.classList.remove('dark');
                localStorage.setItem('color-theme', 'light');
            } else {
                document.documentElement.classList.add('dark');
                localStorage.setItem('color-theme', 'dark');
            }
        }
    });
})();
```

Moving forward I hope to see more sites powered using a frontend `SPA` router and finally put an end to the pesky page refresh.
