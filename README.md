# 3D-Room - An interactive portfolio, from a 3D artist to 3D artists
Progetto: realizzazione di un portfolio per 3D artists, pensato e sviluppato da un 3D artist!

## Descrizione del progetto:
Portfolio online per caricare e mostrare i propri modelli 3D (e relative immagini render) tramite un ambiente virtuale visitabile in first person view.

Il portfolio web che ho realizzato si distingue tra le schede del browser con una favicon. Al primo accesso, il sito presenta un form di login per accedere se già registrati; se non si è registrati, tramite un link presente nella stessa pagina ci si può recare alla pagina con il form di registrazione; la pagina di login contiene anche un link che reinderizza a un modulo di contatto per chiedere modifiche o l'eliminazione del proprio account.

A login avvenuto, si viene reindirizzati alla pagina principale: sono visibili il nome del sito, la propria immagine profilo utente e due pulsanti; il primo reinderizza alla galleria 2D dell'utente, il secondo invece alla galleria 3D dell'utente.

#### Galleria 2D:
La pagina si presenta con un form alla sinistra per caricare le proprie immagini, con la possibilità di attribuire un nome, e con un messaggio di benvenuto a destra, con allegato un pulsante per tornare alla schermata precedente.
Sotto queste sezioni vengono mostrate tutte le immagini caricate dall'utente; passandoci sopra col cursore si attiva la visualizzazione di un pulsante, che consente l'eliminazione della rispettiva immagine.

#### Galleria 3D:
La pagina si presenta come un videogioco in prima persona: ci si ritrova catapultati in un ambiente virtuale, nel quale ci si può muovere con i comandi WASD o con le freccette, e si può orientare la propria visuale con il mouse. Faccio notare che il movimento orizzontale nello spazio 3D è accompagnato da un'oscillazione della camera e da una serie di suoni che si attivano in successione casuale durante il movimento, il tutto per simulare una camminata il più realistica possibile. 
Nella medesima pagina è presente anche quì un form fisso, che però consente questa volta di caricare invece i propri modelli 3D; oltre alla possibilità di attribuirgli un nome, si può scegliere la posizione nella quale lo si vuole visualizzare nel proprio ambiente virtuale, e la scala (lo si può quindi ridimensionare a proprio piacimento).
All'interno della visuale sull'ambiente virtuale è presente una croce, che fa da riferimento alla selezione degli oggetti 3D: tramite la tecnologia del raycasting si possono selezionare gli oggetti 3D nel mondo virtuale. Ho implementato questa funzione per poter mostrare, tramite la comparsa di un popup, le informazioni relative al modello 3D selezionato.

## Tecnologie utilizzate:
* Django
* HTML
* CSS
* Python
* Javascript
* Three.js
* SQLite
### Tecnologie adottate per la sicurezza:
**In questo progetto ho dato particolare importanza alla sicurezza dei dati sensibili:**
* **Gestione Variabili d'Ambiente:** Le informazioni critiche come la `SECRET_KEY` di Django e le configurazioni di `DEBUG` non sono caricate nel codice sorgente.
* **Integrazione Python-Dotenv:** Il progetto utilizza la libreria `python-dotenv` per caricare le configurazioni da un file `.env` locale, che viene escluso dal controllo di versione tramite `.gitignore`.

## Installazione:
1. Clonare (o scaricare) la repository: <br>
`git clone https://github.com/Vale007-web/3D-Room.git`
2. Creare un ambiente virtuale (all'interno della cartella del progetto): <br>
`python -m venv .venv`
3. Attivare l'ambiente virtuale creato: <br>
Su Windows: `.venv\Scripts\activate` <br>
Su Mac/Linux: `source .venv/bin/activate`
4. Installare le dipendenze: <br>
`pip install -r requirements.txt`
5. Configura le variabili d'ambiente: <br>
modifica il file '.env.example' oppure crea un file '.env' nella root del progetto e aggiungi: <br>
   `SECRET_KEY=tua_chiave_segreta` <br>
   `DEBUG=True` <br>
   *(Puoi generare una chiave usando: `python -c 'from django.core.management.utils import get_random_secret_key; print(get_random_secret_key())'`)
6. Esegui le migrazioni e avvia il server: <br>
   `python manage.py migrate` <br>
   `python manage.py runserver` <br>

## DISCLAIMER:
**Il presente progetto è in fase di aggiornamento, per ottimizzare il codice, aggiungere nuove funzioni, e per migliorarlo lato UX e UI**
