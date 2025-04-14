# Django Blog Demo – RESTful Blog App with Docker

Questo progetto è una **demo tecnica Django** pensata per mostrare **competenze concrete nel backend development** con
Django 5.2, Django REST Framework, PostgreSQL, gestione di template e containerizzazione Docker.  
Non contiene codice proprietario o aziendale ed è stato sviluppato per scopi di **portfolio, candidatura o dimostrazione
**.

## 📁 Funzionalità principali

### ✅ Django Core Features

- **Modello `Article`**: con titolo, contenuto, autore (utente), data di pubblicazione automatica.
- **CRUD completo** tramite:
    - **Function-Based Views** (`article_list`) e
    - **Class-Based Views** (`ArticleListView`, `DetailView`, `CreateView`, `UpdateView`, `DeleteView`)
- **Sistema di autenticazione nativo Django** (login/logout richiesto per creare/modificare/eliminare articoli).
- **Template HTML con ereditarietà** (`base.html`) e stile minimale tramite [Pico CSS](https://picocss.com/).

### 🔌 API REST – Django REST Framework

- **Endpoint RESTful** `GET/POST/PUT/DELETE` su `/api/articles/`  
  Implementato tramite `ModelViewSet`.
- **Serializzazione con `ModelSerializer`**.
- **Permessi configurati**: `IsAuthenticatedOrReadOnly`.
- Testato tramite frontend esterno (`fetch()` JavaScript in container separato).

### 🐳 Docker + Docker Compose

- Container **PostgreSQL** (`db`)
- Container **Django** (`web`) con volume montato, porta `8000`, ambiente `.env`
- Container **Nginx static frontend** (`frontend`) per testare le API REST su porta `8080`

### 📌 Note tecniche

- Il container `frontend` è un semplice **Nginx con HTML statico** che effettua `fetch()` verso le API Django.  
  È stato inserito per mostrare **interazione frontend-backend senza framework JS**.

- Il progetto utilizza **PicoCSS** per applicare uno stile minimale e responsive ai template Django.

- La **creazione**, **modifica** e **cancellazione** degli articoli è protetta tramite autenticazione:  
  l'accesso è gestito con **Class-Based View** e **LoginRequiredMixin**.

- Il backend fornisce **API RESTful** pronte all’uso grazie a **Django REST Framework** (`ModelViewSet`).

- Il supporto a **CORS** è abilitato per l'origine `http://localhost:8080`,  
  consentendo l'accesso al backend da parte del frontend statico.

---

## 🚀 Avvio del progetto

1. **Clona la repo:**
   ```bash
   git clone <repo-url>
   cd blogapp
    ```
2. **Configura l'ambiente .env:**
   ```bash
   Troverai un file `.env.template` nella root del progetto. Copialo e rinominalo in `.env`
   ```
3. **Avvia Docker:**
   ```bash
   docker compose up --build
   ```
3. **Applica migrazioni e crea un superuser**
   ```bash
   docker compose exec web python manage.py migrate
   docker compose exec web python manage.py createsuperuser
    ```
