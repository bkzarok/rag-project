import os, requests
from pathlib import Path


OUT = Path("../data/raw"); OUT.mkdir(parents=True, exist_ok=True)
urls = [
    "https://faolex.fao.org/docs/pdf/ssd127441.pdf",
    "https://www.eia.gov/international/content/analysis/countries_long/Sudan_and_South_Sudan/pdf/Sudans%20CAB%20FY2024.pdf",
    "https://verite.org/wp-content/uploads/2021/07/Verite-Country-Report-South-Sudan.pdf",
    "https://www.usip.org/sites/default/files/2021-04/sr_493-conflict_and_crisis_in_south_sudans_equatoria.pdf",
    "https://libraries.indiana.edu/libraries/pdf.js/web/viewer.html?file=https%3A%2F%2Flibraries.indiana.edu%2Fsites%2Fdefault%2Ffiles%2FSOUTH%2520SUDAN.pdf",
    "https://www.u4.no/publications/south-sudan-overview-of-corruption-and-anti-corruption.pdf",
    "https://documents1.worldbank.org/curated/en/099031825031520159/pdf/P500556-9f568594-b30c-4fcc-bb7a-b96df92ed5fd.pdf",
    "https://www.state.gov/wp-content/uploads/2021/03/SOUTH-SUDAN-2020-HUMAN-RIGHTS-REPORT.pdf",
    "https://assets.publishing.service.gov.uk/media/671267b5b40d67191077b398/South_Sudan_Toponymic_Factfile.pdf",
    "https://bti-project.org/fileadmin/api/content/en/downloads/reports/country_report_2022_SSD.pdf",
    "https://era.ed.ac.uk/bitstream/handle/1842/42410/Perceiving-Peace-in-a-Fragment-State-The-Case-of-South-Sudan-DIGITAL.pdf?sequence=1&isAllowed=y",
    "https://www.brookings.edu/wp-content/uploads/2016/06/06-south-sudan.pdf",
    "https://www.cfr.org/sites/default/files/pdf/2016/11/CSR77_Knopf_South%20Sudan.pdf",
    "https://www.ssoar.info/ssoar/bitstream/handle/document/67602/ssoar-jlibertyintaff-2020-1-afriyie_et_al-Comprehensive_analysis_of_South_Sudan.pdf",
    "https://journalistsresource.org/wp-content/uploads/2011/08/South-Sudan.pdf",
    "https://ciaotest.cc.columbia.edu/journals/ambrev/ambrev1257/f_0029920_24220.pdf",
    "https://sgp.fas.org/crs/row/R43344.pdf",
    "https://docs.pca-cpa.org/2016/02/South-Sudan-Peace-Agreement-September-2018.pdf",
    "https://ucdpged.uu.se/peaceagreements/fulltext/SD_120927_Cooperation%20Agreement%20between%20Sudan%20and%20South%20Sudan.pdf",
    "https://www.rahs-open-lid.com/wp-content/uploads/2024/02/South-Sudan_-The-Untold-Story-from-Independence-to-Civil-War-PDFDrive-.pdf",
    "https://carnegie-production-assets.s3.amazonaws.com/static/files/files__sudan_conflict.pdf",
    "https://www.impact-se.org/wp-content/uploads/South-Sudan.pdf",
    "https://eprints.lse.ac.uk/108888/1/McCrone_the_wars_in_South_Sudan_published.pdf",
    "https://med.virginia.edu/family-medicine/wp-content/uploads/sites/285/2018/12/Azobou_South-Sudan-Refugee-Crisis-112018.pdf",
    "https://riftvalley.net/wp-content/uploads/2018/06/RVI-The-Sudan-Handbook.pdf",
    "https://www.congress.gov/crs_external_products/IF/PDF/IF10218/IF10218.14.pdf",
    "https://docs.southsudanngoforum.org/sites/default/files/2018-01/Labour%20Act%202017.pdf",
    "https://mojca.gov.ss/wp-content/uploads/2023/03/Registration-of-Business-Names-Act-7-of-2008.pdf",
    "https://archive.doingbusiness.org/content/dam/doingBusiness/country/s/south-sudan/SSD.pdf",
    "https://www.wto.org/english/thewto_e/acc_e/ssd_e/wtaccssd6_leg_1.pdf",
    "https://mojca.gov.ss/wp-content/uploads/2023/03/Interim-Constitution-of-Southern-Sudan-2005.pdf",
    "https://faolex.fao.org/docs/pdf/ssd127441.pdf",
    "https://www.refworld.org/sites/default/files/attachments/531469ee6.pdf",
    "https://www.homeaffairs.gov.au/foi/files/2021/fa-210700890-document-released.PDF",
    "https://togetherwomenrise.org/wp-content/uploads/2018/08/SouthSudan.pdf",
    "https://faolex.fao.org/docs/pdf/ssd199925.pdf",
    "https://mofaic.gov.ss/wp-content/uploads/2023/03/Investment-Promotion-Act-2009.pdf",
]
for i,u in enumerate(urls,1):
    p = OUT / f"doc_{i:03}.pdf"
    with requests.get(u, timeout=60) as r:
        r.raise_for_status()
        p.write_bytes(r.content)
print("complete")