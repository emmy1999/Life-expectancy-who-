import flask
from flask import request, jsonify
import pandas as pd

app = flask.Flask(__name__)
app.config["DEBUG"] = True
# reading csv file
lf = pd.read_csv("C:/Users/Emmanuel/Documents/MSc DA/Programming/Life Expectancy Data v2.csv")


# homepage
@app.route('/', methods=['GET'])
def home():
    return '''<h1>Life Expectancy Database</h1>
	<p>This is a api for the csv file of Life Expectancy. The project relies on accuracy of data. <br>
    The Global Health Observatory (GHO) data repository under World Health Organization (WHO) keeps track of the health status as well as many other related factors for all countries The data-sets are made available to public for the purpose of health data analysis. </p>'''

# a route to get all data from dataset
@app.route('/api/v1/lf/all', methods=['GET'])
def api_all():
    result = {}
    for index, row in lf.iterrows():
        result[index] = dict(row)
    return jsonify(result)
# a route to filter data based on user request.
@app.route('/api/v1/lf', methods=['GET'])
def api_filter():
    query_parameters = request.args
    
    names = ['Country', 'Year', 'Status', 'Life_Expectancy', 'Adult_Mortality',
       'Infant_Deaths', 'Alcohol', 'Percentage_Expenditure', 'Hepatitis_B',
       'Measles', 'BMI', 'Under-Five_Deaths', 'Polio', 'Total_Expenditure',
       'Diphtheria', 'HIV/AIDS', 'GDP', 'Population', 'Thinness_1-19_Years',
       'Thinness_5-9_Years', 'Income_Composition_of_Resources', 'Schooling']
    
    for param in query_parameters:
        if param not in names:
            return page_not_found(404)    

    # converting the query parameter variable to float or int as per the column type.
    country = query_parameters.get('Country')

    status = query_parameters.get('Status')

    year = query_parameters.get('Year')
    if year:
        year = int(year)

    Life_Expectancy = query_parameters.get('Life_Expectancy')
    if Life_Expectancy:
        Life_Expectancy = float(Life_Expectancy)   
        
    Adult_Mortality = query_parameters.get('Adult_Mortality')
    if Adult_Mortality:
        Adult_Mortality = float(Adult_Mortality)


    infant_d = query_parameters.get('Infant_Deaths')
    if infant_d:
        infant_d = int(infant_d)

    alcohol = query_parameters.get('Alcohol')
    if alcohol:
        alcohol = float(alcohol)

    percent_e = query_parameters.get('Percentage_Expenditure')
    if percent_e:
        percent_e = float(percent_e)

    hepa = query_parameters.get('Hepatitis_B')
    if hepa:
        hepa = float(hepa)

    meas = query_parameters.get('Measles')
    if meas:
        meas = int(meas)

    bmi = query_parameters.get('BMI')
    if bmi:
        bmi = float(bmi)

    under5_d = query_parameters.get('Under-Five_Deaths')
    if under5_d:
        under5_d = int(under5_d)                
    
    polio = query_parameters.get('Polio')
    if polio:
        polio = float(polio)

    total_exp = query_parameters.get('Total_Expenditure')
    if total_exp:
        total_exp = float(total_exp)

    diph = query_parameters.get('Diphtheria')
    if diph:
        diph = float(diph)

    aids = query_parameters.get('HIV/AIDS')
    if aids:
        aids = float(aids)

    gdp = query_parameters.get('GDP')
    if gdp:
        gdp = float(gdp)

    pop = query_parameters.get('Population')
    if pop:
        pop = float(pop)

    thin119yrs = query_parameters.get('Thinness_1-19_Years')
    if thin119yrs:
        thin119yrs = float(thin119yrs)

    thin59yrs = query_parameters.get('Thinness_5-9_Years')
    if thin59yrs:
        thin59yrs = float(thin59yrs)

    income = query_parameters.get('Income_Composition_of_Resources')
    if income:
        income = float(income)

    school = query_parameters.get('Schooling')
    if school:
        school = float(school)

    # filter data based on parameter
    new_lf = lf.copy()


    if country:
        country_lf = new_lf.loc[new_lf['Country'] == country]    
        new_lf = pd.merge(new_lf, country_lf)

    if year:
        year_lf = new_lf.loc[new_lf['Year'] == year]
        new_lf = pd.merge(new_lf, year_lf)
    if status:
        status_lf = new_lf.loc[new_lf['Status'] == status]
        new_lf = pd.merge(new_lf, status_lf)
    if Life_Expectancy:
        Life_Expectancy_lf = new_lf.loc[new_lf['Life_Expectancy'] == Life_Expectancy]    
        new_lf = pd.merge(new_lf, Life_Expectancy_lf)
    if Adult_Mortality:
        Adult_Mortality_lf = new_lf.loc[new_lf['Adult_Mortality'] == Adult_Mortality]  
        new_lf = pd.merge(new_lf, Adult_Mortality_lf)
    
    if infant_d:
        infant_d_lf = new_lf.loc[new_lf['Infant_Deaths'] == infant_d]  
        new_lf = pd.merge(new_lf, infant_d_lf)

    if alcohol:
        alcohol_lf = new_lf.loc[new_lf['Alcohol'] == alcohol]  
        new_lf = pd.merge(new_lf, alcohol_lf)

    if percent_e:
        percent_e_lf = new_lf.loc[new_lf['Percentage_Expenditure'] == percent_e]  
        new_lf = pd.merge(new_lf, percent_e_lf) 

    if hepa:
        hepa_lf = new_lf.loc[new_lf['Hepatitis_B'] == hepa]  
        new_lf = pd.merge(new_lf, hepa_lf) 

    if meas:
        meas_lf = new_lf.loc[new_lf['Measles'] == meas]  
        new_lf = pd.merge(new_lf, meas_lf) 

    if bmi:
        bmi_lf = new_lf.loc[new_lf['BMI'] == bmi]  
        new_lf = pd.merge(new_lf, bmi_lf) 

    if under5_d:
        under5_d = new_lf.loc[new_lf['Under-Five_Deaths'] == under5_d]  
        new_lf = pd.merge(new_lf, percent_e_lf) 

    if polio:
        polio_lf = new_lf.loc[new_lf['Polio'] == polio]  
        new_lf = pd.merge(new_lf, polio_lf) 

    if total_exp:
        total_exp_lf = new_lf.loc[new_lf['Total_Expenditure'] == total_exp]  
        new_lf = pd.merge(new_lf, total_exp_lf) 

    if diph:
        diph_lf = new_lf.loc[new_lf['Diphtheria'] == diph]  
        new_lf = pd.merge(new_lf, diph_lf) 

    if aids:
        aids_lf = new_lf.loc[new_lf['HIV/AIDS'] == aids]  
        new_lf = pd.merge(new_lf, aids_lf) 

    if gdp:
        gdp_lf = new_lf.loc[new_lf['GDP'] == gdp]  
        new_lf = pd.merge(new_lf, gdp_lf)


    if pop:
        pop_lf = new_lf.loc[new_lf['Population'] == pop]  
        new_lf = pd.merge(new_lf, pop_lf) 

    if thin119yrs:
        thin119yrs_lf = new_lf.loc[new_lf['Thinness_1-19_Years'] == thin119yrs]  
        new_lf = pd.merge(new_lf, thin119yrs) 

    if thin59yrs:
        thin59yrs_lf = new_lf.loc[new_lf['Thinness_5-9_Years'] == thin59yrs]  
        new_lf = pd.merge(new_lf, thin59yrs_lf) 

    if income:
        income_lf = new_lf.loc[new_lf['Income_Composition_of_Resources'] == income]  
        new_lf = pd.merge(new_lf, income_lf)  

    if school:
        school_lf = new_lf.loc[new_lf['Schooling'] == school]  
        new_lf = pd.merge(new_lf, school_lf) 


# checking if user request match the parameter or else showing the error page 404.
    if not (year or status or Life_Expectancy or Adult_Mortality or alcohol or country or infant_d or percent_e or hepa
            or meas or bmi or under5_d or polio or total_exp or diph or aids or gdp or pop or 
             thin119yrs or thin59yrs or income or school ):
        return page_not_found(404)
    # returning the result as json 
    result = {}
    for index, row in new_lf.iterrows():
        result[index] = dict(row)
    return jsonify(result)


# error handler for status code 404.
@app.errorhandler(404)
def page_not_found(e):
    return jsonify({'error': 'Bad Request', 'message': str(e)}), 400


app.run()
