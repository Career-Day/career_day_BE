from flask import Flask, request
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
import os

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = "postgresql://postgres:postgres@localhost:5432/career_day"
db = SQLAlchemy(app)
migrate = Migrate(app, db)

if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port)

class JobsModel(db.Model):
    __tablename__ = 'jobs'

    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100), nullable=False)
    icon_url = db.Column(db.String(500), nullable=False)
    image_url = db.Column(db.String(500), nullable=False)
    video_url = db.Column(db.String(500), nullable=False)
    min_salary = db.Column(db.String(500), nullable=False)
    max_salary = db.Column(db.String(500), nullable=False)
    avg_salary = db.Column(db.String(500), nullable=False)
    education = db.Column(db.String(500), nullable=False)
    short_description = db.Column(db.String(1000), nullable=False)
    long_description = db.Column(db.String(2000), nullable=False)

    def __init__(self, title, icon_url, image_url, video_url, min_salary, max_salary, avg_salary, education, short_description, long_description):
        self.title = title
        self.icon_url = icon_url
        self.image_url = image_url
        self.video_url = video_url
        self.min_salary = min_salary
        self.max_salary = max_salary
        self.avg_salary = avg_salary
        self.education = education
        self.short_description = short_description
        self.long_description = long_description

    def __repr__(self):
        return f"Job {self.title}"

@app.cli.command('db_seed')
def db_seed():
    job1 = JobsModel(
        title="Graphic Designer",
        icon_url="https://www.flaticon.com/svg/static/icons/svg/2192/2192721.svg",
        image_url="https://www.freepik.com/blog/app/uploads/2018/07/PIN-BLOG-1270x720-What-is-the-difference-between-an-illustrator-and-a-graphic-designer-1.jpg",
        video_url="https://www.youtube.com/watch?v=kqwgs7vBMkU",
        min_salary="35,000",
        max_salary="60,000",
        avg_salary="47,500",
        education="Bachelor's degree in graphic design",
        short_description="Graphic designers develop graphics and layouts for product illustrations, company logos, websites and more.",
        long_description="Graphic designers are visual communicators, who create visual concepts by hand or by using computer software. They communicate ideas to inspire, inform, or captivate consumers through both physical and virtual art forms that include images, words, or graphics. The end goal of graphic designers is to make the organizations that hire them more well known by their designs. By using a variety of media they communicate a particular idea to be used in advertising and promotions. These media include fonts, shapes, colors, images, print design, photography, animation, logos, and billboards. Graphic designers often work on projects with artists, multimedia animators and other creative professionals."
    )
    job2 = JobsModel(
        title="Software Dev",
        icon_url="https://www.flaticon.com/svg/static/icons/svg/2463/2463510.svg",
        image_url="https://cdn.pixabay.com/photo/2016/09/08/04/12/programmer-1653351_1280.png",
        video_url="https://www.youtube.com/watch?v=_9ZS6q4996g",
        min_salary="60,000",
        max_salary="120,000",
        avg_salary="90,000",
        education="Bachelor's degree in computer Science or trade school",
        short_description="Researching, designing, implementing and managing software programs.",
        long_description="A computer programmer, sometimes called a software developer, a programmer or more recently a coder, is a person who creates computer software. The term computer programmer can refer to a specialist in one area of computers, or to a generalist who writes code for many kinds of software."
    )
    job3 = JobsModel(
        title="Dentist",
        icon_url="https://www.flaticon.com/svg/static/icons/svg/994/994888.svg",
        image_url="https://image.freepik.com/free-vector/dental-clinic-doctor-patient-cartoon-characters-illustration_169479-150.jpg",
        video_url="https://www.youtube.com/watch?v=_Gdozoqzzq0",
        min_salary="130,000",
        max_salary="210,000",
        avg_salary="170,000",
        education="Bachlor's degree and a Doctor of Dental Surgery Degree (DDS) or a Doctor of Medicine in Dentistry Degree (DMD)",
        short_description="Promote and assist in disease prevention and oral health.",
        long_description="Dentists remove tooth decay, fill cavities, and repair fractured teeth. Dentists diagnose and treat problems with patients' teeth, gums, and related parts of the mouth. They provide advice and instruction on taking care of the teeth and gums and on diet choices that affect oral health."
    )
    job4 = JobsModel(
        title="Data Scientist",
        icon_url="https://www.flaticon.com/svg/static/icons/svg/1925/1925173.svg",
        image_url="https://image.freepik.com/free-vector/scientist-people-innovation-laboratory-illustration-cartoon-doctor-character-working-statistic-analysis-white_109722-1592.jpg",
        video_url="https://www.youtube.com/watch?v=_Wk9T_G-u4o",
        min_salary="80,000",
        max_salary="150,000",
        avg_salary="115,000",
        education="Bachelor's degree - computer science, math, economics, statistics.",
        short_description="Data scientists utilize their analytical, statistical, and programming skills to collect, analyze, and interpret large data sets.",
        long_description="Data scientists utilize their analytical, statistical, and programming skills to collect, analyze, and interpret large data sets. They then use this information to develop data-driven solutions to difficult business challenges."
    )
    job5 = JobsModel(
        title="Accountant",
        icon_url="https://www.flaticon.com/svg/static/icons/svg/1925/1925173.svg",
        image_url="https://image.freepik.com/free-vector/consulting-concept-illustration_114360-2719.jpg",
        video_url="https://www.youtube.com/watch?v=8cXZei-7zJI",
        min_salary="30,000",
        max_salary="91,000",
        avg_salary="60,500",
        education="Bachelor's degree minimum, CPA/Master's would be better",
        short_description="Accountants prepare and review financial reports and tax documents.",
        long_description="Accountants prepare and review financial reports and tax documents. Some accountants work for accounting firms and some own their own businesses. Others work for large companies or the government. Accountants work with numbers a lot."
    )
    job6 = JobsModel(
        title="Hair Stylist",
        icon_url="https://www.flaticon.com/svg/static/icons/svg/599/599367.svg",
        image_url="https://image.freepik.com/free-vector/male-hairdressing-beauty-salon-interior-isolated-flat-vector-illustration-cartoon-stylist-beautician-cutting-client-hair-barbershop-appearance-beauty-concept_74855-10100.jpg",
        video_url="https://www.youtube.com/watch?v=Ko37KTlut-A",
        min_salary="20,000",
        max_salary="40,000",
        avg_salary="30,000",
        education="Associate's Degree in Cosmetology",
        short_description="Hair Stylists are beauty service professionals who specialize in the fashioning and treatment of hair.",
        long_description="Hair Stylists are beauty service professionals who specialize in the fashioning and treatment of hair. Hair Stylist responsibilities include cleaning and cutting hair, offering hair care and hair styling consultations and recommending hair styling products, among other duties."
    )
    job7 = JobsModel(
        title="Plumber",
        icon_url="https://www.flaticon.com/svg/static/icons/svg/307/307873.svg",
        image_url="https://image.freepik.com/free-vector/vector-illustration-concept-plumber-service_81522-4780.jpg",
        video_url="https://www.youtube.com/watch?v=OekKI-8S500",
        min_salary="33,000",
        max_salary="98,000",
        avg_salary="65,500",
        education="High School Diploma or equivalnet",
        short_description="A plumber is responsible for installing and repairing water systems in residential or commercial buildings.",
        long_description="Plumbers install and repair plumbing systems in residential and commercial properties. They also install fixtures and domestic appliances associated with heating, cooling, and sanitation systems."
    )
    job8 = JobsModel(
        title="Pediatrician",
        icon_url="https://www.flaticon.com/premium-icon/icons/svg/3323/3323583.svg",
        image_url="https://image.freepik.com/free-vector/gynecology-check-up-illustration_52683-46803.jpg",
        video_url="https://www.youtube.com/watch?v=sBpe7x2rJmo",
        min_salary="153,000",
        max_salary="280,000",
        avg_salary="216,500",
        education="Doctoral Degree",
        short_description="General pediatricians provide care for infants, children, teenagers, and young adults.",
        long_description="General pediatricians provide care for infants, children, teenagers, and young adults. They specialize in diagnosing and treating problems specific to younger people. Most pediatricians treat common illnesses, minor injuries, and infectious diseases, and administer vaccinations. Some pediatricians specialize in pediatric surgery or serious medical conditions that commonly affect younger patients, such as autoimmune disorders or chronic ailments."
    )
    job9 = JobsModel(
        title="Microbiologist",
        icon_url="https://www.flaticon.com/premium-icon/icons/svg/3051/3051239.svg",
        image_url="https://image.freepik.com/free-vector/scientific-research-scientist-people-wearing-lab-coats-science-researches-chemical-laboratory-experiments-illustration_102902-1830.jpg",
        video_url="https://www.youtube.com/watch?v=8OJNXCgIzSM",
        min_salary="44,000",
        max_salary="133,000",
        avg_salary="88,500",
        education="Bachelor's degree",
        short_description="Microbiologists study microorganisms such as bacteria, viruses, algae, fungi, and some types of parasites. They try to understand how these organisms live, grow, and interact with their environments.",
        long_description="Microbiologists study microorganisms such as bacteria, viruses, algae, fungi, and some types of parasites. They try to understand how these organisms live, grow, and interact with their environments. Many microbiologists work in research and development conducting basic research or applied research. Other microbiologists conduct applied research and develop new products to solve particular problems."
    )
    job10 = JobsModel(
        title="Financial Analyst",
        icon_url="https://www.flaticon.com/svg/static/icons/svg/1584/1584961.svg",
        image_url="https://image.freepik.com/free-vector/financial-administration-flat-vector-illustration_82574-8831.jpg",
        video_url="https://www.youtube.com/watch?v=MeFAGixP6NE&ab_channel=CareerOneStop",
        min_salary="48,000",
        max_salary="79,000",
        avg_salary="63,500",
        education="Bachelors Degree in Business or Finance",
        short_description="Financial analysts invariably use spreadsheets (and statistical software packages) to analyze financial data, spot trends, and develop forecasts.",
        long_description="Financial analysts are employed by mutual- and pension funds, hedge funds, securities firms, banks, investment banks, insurance companies, and other businesses, helping these companies or their clients make investment decisions. In corporate roles, financial analysts perform budget, revenue and cost modelling as part of their responsibilities."
    )
    job11 = JobsModel(
        title="Lab Technician",
        icon_url="https://www.flaticon.com/svg/static/icons/svg/3081/3081749.svg",
        image_url="https://image.freepik.com/free-vector/scientist-people-innovation-laboratory-illustration-cartoon-doctors-working-process-robot-creating-white_109722-1591.jpg",
        video_url="https://www.youtube.com/watch?v=tLwKn5W7Bjo&ab_channel=CareerOneStop",
        min_salary="25,000",
        max_salary="45,000",
        avg_salary="35,000",
        education="High School Diploma or Associates Degree",
        short_description="Prepare and in some cases process samples within a laboratory setting.",
        long_description="Lab technicians take raw materials and, using instruments and equipment, shape them into the grounds for conclusions, treatments, and decisions. Learn from the lab technician job description below how experience in this field serves as a foundation for the medical and scientific communities, as well as advanced work in medicine and science."
    )
    job12 = JobsModel(
        title="Zoologist",
        icon_url="https://www.flaticon.com/svg/static/icons/svg/2424/2424348.svg",
        image_url="https://image.freepik.com/free-vector/safari-tourists-enjoying-adventure-travel-watching-animals-taking-pictures-african-landscape-flora-fauna-vector-illustration-jeep-tour-kenya-savannah-journey_74855-8561.jpg",
        video_url="https://www.youtube.com/watch?v=uoyuggwziWA&ab_channel=CareerOneStop",
        min_salary="49,000",
        max_salary="110,000",
        avg_salary="79,500",
        education="Bachelors Degree in Zoology or Wildlife Biology",
        short_description="Zoologists study animals and their interactions with ecosystems.",
        long_description="Zoologists may be involved in a wide variety of duties in various environments. For example they may observe and study animals in their natural environments, or plan and conduct experiments involving animals in nature, in zoos, or in other controlled areas. They may also collect biological specimens and measure physical characteristics. These studies are generally aimed at investigating animal behavior, migration, interactions with other species, and reproduction, as well as the pests, diseases, toxins, and habitat changes that affect them. They use the information they gather to monitor and estimate populations, address invasive species and other threats, control disease, manage hunting programs, and develop conservation plans. They also write reports and journal articles and give presentations to share their findings."
    )
    job13 = JobsModel(
        title="Forensic Accountant",
        icon_url="https://www.flaticon.com/svg/static/icons/svg/1265/1265944.svg",
        image_url="https://image.freepik.com/free-vector/woman-sitting-desk-with-policeman-looking-computer-screen-trying-identify-criminal-using-photo-crime-victim-police-station-flat-cartoon-characters-colorful-vector-illustration_198278-2409.jpg",
        video_url="https://www.youtube.com/watch?v=9CkLxe66Tek",
        min_salary="50,000",
        max_salary="80,000",
        avg_salary="65,000",
        education="Bachelor's or master's degree in forensic accounting, accounting, finance or a related field is required for forensic accountants. Additional education in criminal justice or law enforcement is a plus.",
        short_description="Forensic accountants examine data to determine where missing money has gone and how to recover it. ",
        long_description="Forensic accountants examine data to determine where missing money has gone and how to recover it. They may also present reports of their financial findings as evidence during hearings, where they often testify as expert witnesses. This work serves an important purpose at public accounting and consulting firms, law firms, law enforcement agencies, and insurance companies."
    )
    job14 = JobsModel(
        title="Civil Engineer",
        icon_url="https://www.flaticon.com/premium-icon/icons/svg/2316/2316096.svg",
        image_url="https://image.freepik.com/free-vector/multicultural-team-civil-engineers-construction-site-flat-character-vector-illustration-concept_213110-255.jpg",
        video_url="https://www.youtube.com/watch?v=cJaRjI7K-Lw",
        min_salary="58,000",
        max_salary="121,000",
        avg_salary="89,500",
        education="Bachelor's degree in Engineering",
        short_description="Civil engineers design major transportation projects. ",
        long_description="Civil engineers conceive, design, build, supervise, operate, construct and maintain infrastructure projects and systems in the public and private sector, including roads, buildings, airports, tunnels, dams, bridges, and systems for water supply and sewage treatment."
    )
    job15 = JobsModel(
        title="Pharmacist",
        icon_url="https://www.flaticon.com/svg/static/icons/svg/1256/1256535.svg",
        image_url="https://image.freepik.com/free-vector/customers-pharmacist-pharmacy-store-people-buying-medication-drugstore-flat-vector-illustration-service-treatment-pharmaceutics-concept_74855-9835.jpg",
        video_url="https://www.youtube.com/watch?v=0xxcQQtZKzI",
        min_salary="107,000",
        max_salary="151,000",
        avg_salary="129,000",
        education="Bachlor's degree and a Doctor of Pharmacy (PharmD).",
        short_description="Provide medical advice and dispense medications. ",
        long_description="Pharmacists are healthcare practitioners who check and distribute drugs to doctors for medication that had been prescribed to patients. They advise patients and health care providers on the selection, dosages, interactions, and side effects of medications. They might work in a  hospital or retail store."
    )
    jobs = [job1, job2, job3, job4, job5, job6, job7, job8, job9, job10, job11, job12, job13, job14, job15]
    for job in jobs:
        db.session.add(job)
    db.session.commit()
    print('Database seeded!')

@app.route('/jobs')
def handle_jobs():
    jobs = JobsModel.query.all()
    results = [
        {
        "avg_salary": job.avg_salary,
        "education": job.education,
        "icon_url": job.icon_url,
        "id": job.id,
        "short_description": job.short_description,
        "title": job.title
        } for job in jobs]

    return {"jobs": results}

@app.route('/job/<job_id>')
def handle_job(job_id):
    job = JobsModel.query.get_or_404(job_id)

    response = {
        "education": job.education,
        "id": job.id,
        "image_url": job.image_url,
        "long_description": job.long_description,
        "max_salary": job.max_salary,
        "min_salary": job.min_salary,
        "title": job.title,
        "video_url": job.video_url
    }
    return {"job": response}
