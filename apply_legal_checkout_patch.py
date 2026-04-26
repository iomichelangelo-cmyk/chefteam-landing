from pathlib import Path
import re

path = Path("index.html")
html = path.read_text(encoding="utf-8")

Path("index.backup-legal-checkout.html").write_text(html, encoding="utf-8")

html = html.replace("€6,90", "€7,90")
html = html.replace("Perfetto per iniziare con flessibilità", "10 giorni di prova gratuita, poi €7,90/mese")

html = html.replace(
    'href="https://wa.me/393931423221?text=Ciao%20ChefTeam%20voglio%20iniziare"',
    'href="https://chefteam.lemonsqueezy.com/checkout"'
)

footer_new = """<footer class="footer">
    <div class="container">
      <div style="margin-bottom:10px">
        <a href="./privacy.html">Privacy</a> ·
        <a href="./cancellazione-dati.html">Cancellazione dati</a> ·
        <a href="./cookie-policy.html">Cookie policy</a>
      </div>
      © 2026 ChefTeam. Tutti i diritti riservati.
    </div>
  </footer>"""

html = re.sub(r'<footer class="footer">.*?</footer>', footer_new, html, count=1, flags=re.S)

start = html.find('<section class="section founder">')
if start != -1:
    next_section = html.find('<section', start + 10)
    main_end = html.find('</main>', start)
    end = next_section if next_section != -1 and next_section < main_end else main_end
    founder = """<section class="section founder">
      <div class="container two-col">
        <div>
          <div class="badge">Chi ha creato ChefTeam</div>
          <h2 class="serif">ChefTeam nasce da una sveglia vera</h2>
          <p>Dopo le feste avevo preso 5 kg. Ho avuto problemi di pressione alta, mi sono spaventato e ho capito una cosa semplice: non sapevo davvero come mangiare bene.</p>
          <p>Ero sempre stato sovrappeso senza capire fino in fondo perché. Non sapevo come abbinare proteine, carboidrati, grassi e verdure. Non sapevo regolarmi con le quantità. Cucinavo sempre le stesse cose e, quando volevo cambiare, non sapevo da dove partire.</p>
          <p>Ho provato anche con l’AI, ma ogni volta dovevo ricominciare da zero: rispiegare i miei gusti, le mie preferenze, i miei obiettivi, quello che avevo già mangiato e quello che volevo evitare.</p>
          <p>Da lì è nata l’idea di ChefTeam: un assistente su WhatsApp che ti aiuta a organizzare menu e spesa, ma soprattutto si ricorda di te.</p>
          <p>Nel mio caso, con più ordine a tavola e allenamento, ho perso 14 kg in 3 mesi, la pressione è tornata perfetta e sono tornato al peso che avevo a 20 anni.</p>
          <p>ChefTeam non nasce per promettere miracoli. Nasce per rendere più semplice una cosa che per tante persone è sempre stata complicata: sapere cosa mangiare, cosa comprare e come restare costanti.</p>
        </div>

        <div class="large-photo tall">
          <img src="./images/founder.jpeg" alt="Founder di ChefTeam">
        </div>
      </div>
    </section>

    """
    html = html[:start] + founder + html[end:]

path.write_text(html, encoding="utf-8")
print("OK: index.html aggiornato con prezzo, checkout Lemon, footer legale e founder story.")
