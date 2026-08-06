
mkdir templates 
python3 scaffold.py plane_ticket depart destination
python3 scaffold.py resume person_id:references content phone email
python3 scaffold.py person name phone email
python3 scaffold.py company name phone email
python3 scaffold.py linkpersoncompany person_id:references company_id:references
python3 scaffold.py musicsession name description
python3 scaffold.py participantjamuser musicsession_id:references user_id:references
python3 scaffold.py participantjamperson musicsession_id:references person_id:references
python3 scaffold.py city name
python3 scaffold.py resume_matcher resume1_id resume2_id description
python3 scaffold.py concert time date place title city_id:references
python3 scaffold.py user username email password phone country_id:references
python3 scaffold.py concert_ticket promotion_name price concert_id:references user_id:references
