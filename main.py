from pyrogram import Client, filters
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from datetime import datetime
import time
from apscheduler.schedulers.background import BackgroundScheduler
from datetime import timedelta

# === CONFIGURAZIONE BOT ===
api_id = 25528984
api_hash = "cf3ebabd1bec07a61329215f8727ddd0"
bot_token = "7625619912:AAHAhAq_9ZKB9BQEcRhVjM3BE9d48-jHOOk"
app = Client("numerobot", api_id=api_id, api_hash=api_hash, bot_token=bot_token)
scheduler = BackgroundScheduler()
scheduler.start()


# === CONSULTI PER OGNI NUMERO ===
consulti = {
    "1": {
         "base": "✨Anno Personale 1: Un Nuovo Inizio - L’Anno Personale 1 segna l’inizio di un nuovo ciclo nella tua vita, un capitolo di rinnovamento che ti invita a prendere il comando del tuo destino. Dopo il periodo di chiusura e riflessione dell’Anno 9, ora è il momento di concentrarti su ciò che desideri davvero e di costruire le basi per il tuo futuro. Questa energia ti sprona ad abbracciare la tua autonomia, a mettere in gioco il tuo coraggio e a intraprendere nuovi percorsi con determinazione. È l’anno per fissare obiettivi ambiziosi e per avere fiducia nelle tue capacità di realizzarli.",
                "amore": "💖L’Anno Personale 1 in amore porta un’energia di rinnovamento e indipendenza nelle relazioni. Se sei in coppia, questo è il momento per ridefinire il tuo rapporto, dando priorità a un equilibrio sano tra autonomia personale e connessione emotiva.Se sei single, l’energia del 1 ti offre un’opportunità unica per concentrarti su te stessa e per chiarire cosa desideri davvero in una relazione.",
                "successo": "💼 L’Anno Personale 1 è il tuo trampolino di lancio per creare nuove basi nella tua carriera e nelle tue finanze. Questa energia ti offre una carica di motivazione e coraggio per prendere il controllo del tuo destino professionale. Hai grinta, forza decisionale e spirito d'iniziativa. È il momento per lanciare progetti, cambiare carriera o prendere decisioni importanti. I risultati non arriveranno subito, ma le basi che costruisci ora avranno un impatto duraturo.",
                "sfida": "⚠️L’Anno Personale 1, se vissuto in negativo, può trasformare l’energia del rinnovamento in un periodo di confusione e stallo. Potresti sentirti sopraffatta dal desiderio di iniziare nuovi progetti ma bloccata dalla paura di fallire. L’impazienza potrebbe prendere il sopravvento. La tua sfida sarà non bloccarti per il timore del giudizio. Agisci con determinazione anche se l’approvazione esterna tarda ad arrivare. Evita di isolarti e chiedi supporto quando serve."
            },
            "2": {
                "base": "✨L’Anno Personale 2 rappresenta una fase di equilibrio, connessione e crescita emotiva. Dopo l’energia di inizio e indipendenza dell’Anno 1, ora entri in un periodo in cui il focus si sposta dalla tua individualità verso la collaborazione e il sostegno reciproco. L’energia del 2 è delicata, sensibile e orientata verso il costruire relazioni più profonde, che siano personali, professionali o persino spirituali. È un anno in cui l’empatia e la pazienza diventano le tue alleate più preziose.",
                "amore": "💖L’Anno Personale 2 porta le relazioni al centro della tua attenzione. Dopo un periodo di forte indipendenza e nuovi inizi, ora sei chiamata a costruire legami autentici e a nutrire le connessioni che contano davvero.Se sei in coppia, l’energia del Numero 2 favorisce il rafforzamento della relazione. Potresti trovare il desiderio di aprirti maggiormente al dialogo e di lavorare insieme per costruire un rapporto più equilibrato e armonioso.Se sei single, l’Anno 2 potrebbe portare incontri significativi e connessioni profonde.",
                "successo": "💼 L’Anno Personale 2 è una fase che ti incoraggia a mettere da parte l’individualismo dell’Anno 1 per abbracciare il potere della collaborazione. In ambito lavorativo, la chiave del successo sarà il lavoro di squadra, l’empatia e la capacità di costruire relazioni autentiche.Evita i colpi di testa e punta sul lavoro di squadra. È l’anno della diplomazia, non del comando. Fai crescere le collaborazioni e costruisci alleanze solide. I riconoscimenti arriveranno nei prossimi cicli.",
                "sfida": "⚠️L’Anno Personale 2, con la sua energia di connessione e sensibilità, può diventare una sfida se vissuto in negativo. Invece di portare equilibrio e armonia, potresti trovarti sopraffatta dall’eccessiva emotività e dalle richieste degli altri. Questo potrebbe tradursi in una sensazione di instabilità, come se le tue emozioni ti sfuggissero di mano.Attenzione alla passività o alla tendenza ad assorbire le emozioni degli altri. Non trascurarti per “compiacere”. Stabilisci confini sani."
            },
            "3": {
                "base": "✨L’Anno Personale 3 rappresenta un capitolo di espansione, creatività e celebrazione nella tua vita. Dopo il periodo di introspezione e collaborazione dell’Anno 2, ora entri in una fase più luminosa e dinamica, in cui l’espressione personale diventa centrale. È un anno in cui ti viene chiesto di abbracciare la tua autenticità e di esplorare nuove modalità per condividere il tuo talento con il mondo. Che si tratti di comunicazione, arte o semplicemente della tua energia, il 3 ti invita a metterti in gioco senza riserve.",
                "amore": "💖L’Anno Personale 3 porta una ventata di freschezza, gioia e rinnovamento nelle relazioni, invitandoti a vivere i tuoi rapporti con leggerezza e spontaneità. Se sei in coppia, questo è il momento ideale per ravvivare la tua connessione attraverso esperienze che rompono la monotonia della quotidianità.Se sei single, l’energia del 3 accresce il tuo carisma e la tua capacità di attrarre persone nuove.",
                "successo": "💼La creatività e l’espressione personale saranno le tue armi vincenti in ambito lavorativo durante l’Anno Personale 3. Questo periodo ti offre l’opportunità di emergere grazie alla tua capacità di pensare fuori dagli schemi e proporre soluzioni innovative.Espandi la tua rete, comunica, fai conoscere il tuo lavoro. È l’anno ideale per social media, eventi, collaborazioni creative. Sfrutta il tuo carisma per attrarre occasioni.",
                "sfida": "⚠️L’Anno Personale 3 porta con sé un’energia frizzante e piena di entusiasmo, ma se vissuto in negativo, può trasformarsi in un periodo di instabilità e dispersione. Potresti ritrovarti sopraffatta dalla voglia di fare tutto e subito, iniziando tanti progetti senza completarli."
            },
            "4": {
                "base": "✨L’Anno Personale 4 rappresenta un periodo di costruzione, impegno e realizzazione concreta. Dopo le energie più fluide e relazionali dell’Anno 3, ora entri in una fase che ti richiede stabilità e concentrazione. È un anno in cui sei chiamata a rimboccarti le maniche e a dedicarti con disciplina ai tuoi obiettivi. La parola chiave è “costruzione”: tutto ciò che fai ora getta le fondamenta per i successi futuri.",
                "amore": "💖L’Anno Personale 4 porta un’energia di stabilità e impegno nelle relazioni. Se sei in coppia, questo è il momento per rafforzare la vostra connessione lavorando insieme verso obiettivi condivisi. Se sei single, l’Anno 4 potrebbe sembrare meno orientato alle nuove connessioni romantiche, ma non è così. Questo è un anno in cui potresti incontrare qualcuno che condivide i tuoi valori e il desiderio di costruire qualcosa di concreto.",
                "successo": "💼L’Anno Personale 4 rappresenta un momento cruciale per costruire la tua stabilità finanziaria e professionale. È un anno in cui il lavoro metodico e la pianificazione strategica saranno fondamentali per raggiungere i tuoi obiettivi.Metti a punto la tua visione. Costruisci con metodo. È l’anno per creare sistemi e routine efficaci. Ottimo per sistemare finanze e organizzazione.",
                "sfida": "⚠️L’Anno Personale 4, se vissuto in negativo, può trasformare il desiderio di costruzione e stabilità in rigidità e sovraccarico. Potresti sentirti intrappolata nella routine, come se il peso delle responsabilità fosse troppo grande da sostenere. Il rischio è di cadere nel perfezionismo, cercando di controllare ogni dettaglio senza lasciare spazio alla flessibilità. Non dimenticare il cuore mentre strutturi la mente."
            },
            "5": {
                "base": "✨L’Anno Personale 5 è sinonimo di cambiamento, movimento e spontaneità. Dopo le basi poste negli anni precedenti, adesso sei chiamata a sperimentare con coraggio e a esplorare territori nuovi. L’energia del 5 accelera il ritmo della vita, spingendoti a vivere con più intensità e a cogliere le occasioni che si presentano, anche quando sembrano fuori dalla tua zona di comfort.",
                "amore": "💖Durante l’Anno Personale 5, le relazioni diventano un campo di sperimentazione e scoperta. Dopo un periodo più stabile o riflessivo, adesso cerchi novità anche sul piano affettivo. Se sei in coppia, potresti avvertire il bisogno di rivitalizzare il rapporto, magari progettando viaggi insieme o introducendo nuove attività che rompano la monotonia. Se sei single, il 5 offre innumerevoli occasioni di incontro. È un anno ideale per allargare i tuoi orizzonti sociali e lasciarti sorprendere da nuove conoscenze.",
                "successo": "💼Nel lavoro, l’Anno Personale 5 porta una ventata di cambiamento e opportunità di crescita rapida. Potresti ricevere proposte inaspettate, decidere di metterti in proprio oppure di modificare radicalmente la tua carriera. È l’anno dei cambiamenti professionali. Potresti cambiare direzione, viaggiare, iniziare nuovi progetti. Ottimo per il marketing, la comunicazione, il pubblico.",
                "sfida": "⚠️L’Anno Personale 5, se vissuto in maniera squilibrata, può portare a una sensazione di caoticità e di mancanza di direzione. L’impulsività potrebbe spingerti a fare scelte azzardate, compromettendo relazioni, lavoro o stabilità finanziaria. Resta focalizzata. Non tutto il nuovo è giusto per te."
            },
            "6": {
                "base": "✨L’Anno Personale 6 si distingue per la sua energia di armonia, dedizione e responsabilità. Dopo aver sperimentato cambiamenti e slanci di individualità negli anni precedenti, adesso entri in una fase in cui il benessere delle relazioni e la ricerca di un equilibrio personale diventano protagonisti. Il 6 rappresenta un invito a prenderti cura non solo di chi ami, ma anche di te stessa: è un periodo in cui la famiglia, la casa e gli affetti hanno un ruolo centrale nella tua vita.",
                "amore": "💖In un Anno Personale 6, l’attenzione si focalizza sulle connessioni emotive, sul senso di appartenenza e sulla necessità di costruire legami solidi e appaganti.Anno perfetto per ufficializzare relazioni, fare scelte importanti, accogliere nuove anime nella tua vita. L’amore chiede verità, dedizione e ascolto.Se sei in coppia, potresti sentire il desiderio di rafforzare la relazione, rendendola più solida e significativa.Se sei single, questo anno porta con sé un’energia che favorisce incontri significativi, basati su affinità profonde e condivisione di valori.",
                "successo": "💼 Nell’ambito professionale, l’Anno 6 si traduce in un approccio collaborativo e orientato al benessere collettivo. Questo è un periodo in cui il lavoro di squadra assume un ruolo centrale e in cui potresti sentire il bisogno di operare in un ambiente più sereno e armonioso, dove la qualità delle relazioni conta tanto quanto il raggiungimento degli obiettivi. Progetti creativi o legati al benessere possono decollare. Lavora sull’equilibrio tra dare e ricevere.",
                "sfida": "⚠️Se mal gestita, l’energia del 6 può portare a sentirti sopraffatta dalle richieste di chi ti sta intorno o a sviluppare un perfezionismo esagerato. Potresti cadere nella trappola di voler risolvere i problemi di tutti, finendo per trascurare la tua serenità. In alcuni casi, la tendenza a mediare può sfociare in un atteggiamento di autosacrificio, con il rischio di reprimere i tuoi veri desideri. Non mettere i bisogni altrui prima dei tuoi."
            },
            "7": {
                "base": "✨L’Anno Personale 7 rappresenta una fase di profonda introspezione e di ricerca del significato più autentico della vita. Dopo aver sperimentato l’energia collaborativa e “familiare” dell’Anno 6, senti ora il bisogno di rallentare e di comprendere meglio il tuo mondo interiore. Il 7 è spesso associato alla spiritualità e alla conoscenza: è l’anno in cui potresti sentire il richiamo di discipline filosofiche, scientifiche o esoteriche che possano aiutarti a esplorare l’essenza delle cose.",
                "amore": "💖 Nell’Anno Personale 7, l’approfondimento diventa la parola chiave in ogni ambito della vita, compresi gli affetti. Questo è un periodo di autoanalisi e crescita interiore, in cui potresti sentire il bisogno di rivedere le tue relazioni sotto una nuova luce, chiedendoti quanto siano realmente in sintonia con la tua evoluzione personale. Se sei in coppia, potresti avvertire l’esigenza di un maggiore spazio mentale ed emotivo per riflettere su ciò che vuoi realmente dalla relazione. Se sei single, il numero 7 ti porta a cercare relazioni di qualità, basate su affinità spirituale, intellettuale ed emotiva. Potresti non avere interesse per flirt superficiali o storie di breve durata, preferendo invece poche ma significative connessioni.",
                "successo": "💼In ambito lavorativo, l’Anno Personale 7 porta con sé un forte desiderio di ricerca, approfondimento e specializzazione. Questo è un periodo in cui potresti sentirti particolarmente attratta da percorsi di crescita intellettuale e professionale, spingendoti a migliorare le tue competenze e ad acquisire nuove conoscenze. Le risposte arrivano dal silenzio. Non forzare i risultati.",
                "sfida": "⚠️Se l’energia del 7 viene vissuta in modo squilibrato, potresti scivolare verso un eccesso di introspezione, trasformando la ricerca interiore in un auto-isolamento. La critica, rivolta a te stessa o agli altri, potrebbe farsi più dura, alimentando sentimenti di frustrazione o inadeguatezza."
            },
            "8": {
                "base": "✨Potere, abbondanza, realizzazione.L’Anno Personale 8 è una fase di realizzazione concreta, in cui tutto ciò che hai seminato negli anni precedenti può finalmente dare frutti tangibili. L’8 rappresenta l’energia dell’ambizione, della responsabilità e del successo: ti troverai a dover gestire risorse importanti (finanziarie, professionali o umane), e questo ti darà la possibilità di ottenere risultati considerevoli.",
                "amore": "💖 L’Anno Personale 8, con la sua forte aura di leadership, ambizione e determinazione, lascia il segno anche nelle dinamiche affettive. Questo è un periodo in cui potresti sentirti spinta a “mettere ordine” nelle tue relazioni, cercando un dialogo più maturo, stabile e definendo obiettivi condivisi.Se sei in coppia, una delle principali sfide dell’Anno 8 è evitare di trascurare gli affetti e la sfera emotiva a causa di carichi di lavoro più intensi o di una maggiore focalizzazione sugli obiettivi personali. Se sei single, l’energia dell’8 potrebbe attrarti verso persone che rispecchiano la tua ambizione e il tuo desiderio di successo.",
                "successo": "💼Questo è l’anno in cui puoi concretizzare molte delle idee e dei progetti che hai maturato negli ultimi anni. Grazie a una rinnovata capacità di focalizzarti sugli obiettivi, questo periodo ti offre la possibilità di trasformare la tua visione in realtà tangibile. L’energia dell’8 è strettamente legata al successo, alla realizzazione e all’espansione, portando opportunità di crescita sia sul piano personale che professionale. Hai tutte le carte in regola per avanzare: promozioni, successi, nuove posizioni. Ma tutto dipenderà dalla tua etica.",
                "sfida": "⚠️ Ambizione senza radici. Se l’energia dell’8 è vissuta in squilibrio, potresti cadere nell’ossessione del controllo, diventando rigida e poco flessibile. Lo stress può raggiungere livelli molto alti, sfociando in burn-out, litigi con collaboratori o incomprensioni in famiglia."
            },
            "9": {
                "base": "✨L’Anno Personale 9 simboleggia un vero e proprio canto del cigno di un ciclo durato nove anni. È un periodo di conclusione, in cui diverse situazioni della tua vita – lavorative, affettive, abitative – potrebbero giungere al termine. Più che spaventarti, questo invito alla “chiusura” può trasformarsi in un momento di profonda liberazione: ciò che non è più in sintonia con la tua evoluzione cade via, lasciandoti lo spazio necessario per abbracciare il nuovo, che emergerà pienamente nell’Anno Personale 1.",
                "amore": "💖Potresti affrontare chiusure o trasformazioni nelle relazioni. Nell’Anno Personale 9, le dinamiche relazionali possono oscillare tra la necessità di risolvere o chiudere rapporti stagnanti e la voglia di esprimere un amore più ampio, quasi “universale”.Se sei in coppia, il 9 può portare fasi di riflessione: forse tu e il tuo partner state concludendo una tappa del percorso di coppia per aprirvene un’altra, più profonda.Se sei single, potresti mettere un punto fermo al desiderio di vivere relazioni superficiali o ripetitive.",
                "successo": "💼Conclusioni importanti. Non iniziare nulla di nuovo troppo impegnativo. Sul piano professionale, il 9 tende a evidenziare la necessità di chiudere progetti, incarichi o collaborazioni che hanno esaurito la loro spinta creativa. Se stai inseguendo un obiettivo da tempo, potresti finalmente portarlo a termine e raccogliere i risultati",
                "sfida": "⚠️Se l’energia del 9 è vissuta in modo squilibrato, potresti resistere al cambiamento, rifiutando di chiudere situazioni ormai esauste. Questo può creare un senso di stagnazione e malinconia, facendoti restare in rapporti o ruoli che non ti fanno crescere."
            }
        }

# === DATI UTENTE ===
user_data = {}

# === /START: BENVENUTO ===
from datetime import datetime, timedelta

@app.on_message(filters.command("start"))
def start(client, message):
    chat_id = str(message.chat.id)
    user_data[chat_id] = {
        "fase": "nome",
        "start_time": datetime.now().isoformat(),
        "followup1_sent": False,
        "followup2_sent": False
    }
    save_data()
    message.reply(
        "✨ Ciao MANIFESTER ✨\n\n"
        "Come ti chiami? Scrivilo qui sotto per iniziare il tuo percorso numerologico!! 💖"
    )

# === GESTIONE NOME + DATA ===
@app.on_message(filters.text & ~filters.command("start"))
def get_data(client, message):
    chat_id = str(message.chat.id)
    text = message.text.strip()

    if chat_id not in user_data:
        return  # ignora messaggi da utenti che non hanno fatto /start

    fase = user_data[chat_id].get("fase")

    if fase == "nome":
        user_data[chat_id]["nome"] = text
        user_data[chat_id]["fase"] = "data"
        save_data()
        message.reply(f"Grazie ✨ Ciao {text.upper()} ✨\n\nOra dimmi la tua **data di nascita** nel formato GG/MM/AAAA")
        return

    elif fase == "data":
        try:
            giorno, mese, anno = map(int, text.split("/"))
            anno_corrente = datetime.today().year
            numero = riduci(somma(f"{giorno}{mese}{anno_corrente}"))
            user_data[chat_id]["data"] = text
            user_data[chat_id]["numero"] = str(numero)
            user_data[chat_id]["fase"] = "completato"
            save_data()

            client.send_video(chat_id, f"{numero}.mp4")

            message.reply(
                f"🔢 Il tuo **Anno Personale è: {numero}**\n\n"
                f"{consulti[str(numero)]['base']}"
            )

            client.send_message(
                chat_id,
                "Ora che hai scoperto il numero del tuo anno personale 🌟 "
                "che va dal tuo compleanno 2025 al 2026...\n\n"
                "💖Andiamo più in profondità… Sei pronta per scoprire cosa ti riserverà quest’anno nella sfera dell’AMORE E DELLE RELAZIONI?",
                reply_markup=InlineKeyboardMarkup([
                    [InlineKeyboardButton("💖 Sì, sono pronta!", callback_data="amore")]
                ])
            )
        except Exception:
            message.reply("❗️Formato non valido. Inserisci la data così: GG/MM/AAAA (es. 14/08/1991)")
        return

    elif fase == "completato":
        # Blocco ulteriore spam
        return

# === BOTTONI: RISPOSTE DETTAGLIATE ===
@app.on_callback_query()
def handle_buttons(client, callback_query):
    chat_id = callback_query.message.chat.id
    numero = user_data.get(chat_id, {}).get("numero", "1")
    scelta = callback_query.data

    if scelta == "amore":
        client.send_message(
            chat_id,
            f"Ecco la tua previsione in amore:\n\n{consulti[numero]['amore']}\n\n"
            "🌟 Passiamo ora a un’altra sfera importante... Vuoi scoprire cosa ti aspetta sul piano del SUCCESSO e delle OPPORTUNITÀ?",
            reply_markup=InlineKeyboardMarkup([
                [InlineKeyboardButton("Sì, voglio scoprirlo✨", callback_data="successo")]
            ])
        )

    elif scelta == "successo":
        time.sleep(3)
        client.send_message(
            chat_id,
            f"Ecco la tua previsione per la sfera lavorativa e successo: \n\n{consulti[numero]['successo']}"
            
             "Ma ogni numero porta anche una sfida da trasformare in evoluzione, vuoi sapere qual è la tua sfida dell’anno?",
            reply_markup=InlineKeyboardMarkup([
                [InlineKeyboardButton("⚠️Sì, voglio conoscerla", callback_data="sfida")]
            ])
        )

    elif scelta == "sfida":
        time.sleep(3)
        client.send_message(
            chat_id,
            f"Ecco la tua previsione per le sfide che potrebbero presentarsi quest'anno: \n\n{consulti[numero]['sfida']}"
            
            "📚 Ma non è finita qui..Ho preparato per te una guida approfondita.",
            reply_markup=InlineKeyboardMarkup([
                [InlineKeyboardButton("📚 Scopri la Lettura Completa", callback_data="offerta")]
            ])
        )

    elif scelta == "offerta":
        time.sleep(3)
        client.send_message(
            chat_id,
            "📚 *Ho preparato per te la lettura completa di* **Unlock Your Destiny – Personal Year** ✨\n\n"
            "✅ Oltre 60 pagine personalizzate con mese per mese\n"
            "✅ Rituali, consigli di manifestazione e guida energetica\n\n"
            "🌟Non è solo una lettura. È una vera e propria bussola sacra per navigare con consapevolezza il tuo Anno Personale. Se senti che è il tuo momento di fare chiarezza, attivare il tuo potere interiore e manifestare con fiducia...Questa guida è stata scritta per te.",
            reply_markup=InlineKeyboardMarkup([
                [InlineKeyboardButton("🔓 Accedi subito alla Lettura Personal Year", url="https://6786deff92dd1.site123.me/")]
            ])
        )

        time.sleep(6)
        client.send_message(
            chat_id,
            "🔮 *Ma non è finita qui…* 🌌\n\n"
            "✨ La mia lettura numerologica si unisce perfettamente alla *Rivoluzione Solare Astrologica*,\n"
            "offrendoti una mappa completa del tuo anno da compleanno a compleanno.\n\n"
            "💫 Insieme ti aiutano a:\n"
            "🌕 Capire sfide e doni karmici\n"
            "🌈 Navigare relazioni, opportunità e cambiamenti\n"
            "🧭 Manifestare con più consapevolezza",
            reply_markup=InlineKeyboardMarkup([
                [InlineKeyboardButton("🌗 Attiva la COMBO NUMERO + RS", url="https://buy.stripe.com/9AQaFJ5x13EUbPG8wG")]
            ])
        )

    else:
        callback_query.message.reply("Ops, qualcosa è andato storto 😅")

# === FUNZIONI NUMEROLOGIA ===
def somma(s):
    return sum(int(c) for c in s if c.isdigit())

def riduci(n):
    while n > 9 and n not in [11, 22]:
        n = sum(int(c) for c in str(n))
    return n

# === FOLLOW-UP: MESSAGGI PROGRAMMATI (24h e 48h) ===
def controlla_followup():
    now = datetime.now()
    
    for chat_id, dati in user_data.items():
        start_time_str = dati.get("start_time")
        if not start_time_str:
            continue  # ⛔️ Se non c'è un timestamp di inizio, salta

        start_time = datetime.fromisoformat(start_time_str)
        elapsed = now - start_time

        # ⏰ DOPO 24 ORE - Primo follow-up (testo)
        if elapsed > timedelta(hours=24) and not dati.get("followup1_sent"):
            app.send_message(
                chat_id,
                "🕰 È passato un giorno… ma l’energia del tuo Anno Personale è ancora qui.\n"
                "Forse hai già iniziato a sentire certe vibrazioni dentro di te…\n\n"
                "✨ Se senti che questo è il momento giusto per chiarire, allinearti e manifestare…\n\n"
                "📚 La Lettura Numerologica Completa è ancora disponibile per te.\n"
                "⚠️ *I posti sono limitati e la scorsa volta è andata sold out in soli 2 giorni!*\n\n"
                "🔓 Accedi subito alla guida personalizzata:\n"
                "https://6786deff92dd1.site123.me/"
            )
            dati["followup1_sent"] = True
            save_data()

        # ⏳ DOPO 48 ORE - Secondo follow-up (con immagine)
        elif elapsed > timedelta(hours=48) and not dati.get("followup2_sent"):
            app.send_photo(
                chat_id,
                photo="testimonianza.jpg",
                caption=(
                    "📬 Ecco una delle testimonianze che abbiamo ricevuto sulla Lettura Personal Year:\n\n"
                    "_\"Io sono sbalordita. Sto sfruttando l'energia del mio anno personale "
                    "e ho inziato a realizzare manifestazione della mia Vision Board!\"_\n\n"
                    "💫 Se ancora non hai scaricato la tua copia personalizzata, il momento è adesso.\n\n"
                    "🔓 Accedi subito alla guida:\n"
                    "https://6786deff92dd1.site123.me/"
                )
            )
            dati["followup2_sent"] = True
            save_data()
# Programmazione messaggi
scheduler.add_job(controlla_followup, "interval", minutes=10)

# === AVVIO BOT ===
from keep_alive import keep_alive
keep_alive()

app.run()
