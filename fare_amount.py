import streamlit as st
import pickle
import numpy as np
model=pickle.load(open('model.pkl','rb'))
def distance( PULocationID_11 ,DOLocationID_11,PULocationID_22, DOLocationID_22):
    lon1, lat1, lon2, lat2 = map(np.radians, [PULocationID_11 ,DOLocationID_11,PULocationID_22, DOLocationID_22])
    dlon = lon2 - lon1
    dlat = lat2 - lat1
    a = np.sin(dlat/2.0)**2 + np.cos(lat1) * np.cos(lat2) * np.sin(dlon/2.0)**2
    c = 2 * np.arcsin(np.sqrt(a))
    km = 6367 * c
    return km         
                   
def predict_fareamount(congestion_surcharge,distance,pickup_day_no,pickup_hour, AWND, PRCP, SNOW, SNWD, TMAX, TMIN,work_hour,work_day ):
    input=np.array([[congestion_surcharge,distance,pickup_day_no,pickup_hour, AWND, PRCP, SNOW, SNWD, TMAX, TMIN,work_hour,work_day]]).astype(np.float64)
    prediction=model.predict(input)
    pred='{0:.{1}f}'.format(prediction[0][0], 2)
    return float(pred)
def main():
    
    st.title(" Fare Amount Prediction in NYC Trips!")
    congestion_surcharge1 = st.number_input("congestion surcharge :")
    hour = st.number_input('Hour : ')
    day= st.number_input('Day :')
    PULocation_lon=st.number_input('Departure Location longitude : ')
    PULocation_lat=st.number_input('Departure Location latitude : ')
    DOLocationID_lon=st.number_input('Access Location longitude : ')
    DOLocationID_lat=st.number_input('Access Location latitude : ')
    distancen =distance( PULocation_lon ,PULocation_lat,DOLocationID_lon, DOLocationID_lat)
    awnd=4.47
    prcp=0.27
    snow=0.0
    snwd=0.0
    tmax=51
    tmin=41
    if (day == 5)|(day == 6):
        work_day= 0
    else:
        work_day=1
    if hour in[ 7,8,9,16,17,18,19] :
        work_hour= 1
    else:
        work_hour=0
    if st.button("Predict"):      
        output=predict_fareamount(congestion_surcharge1,distancen,day,hour, awnd,prcp,snow,snwd,tmax,tmin,work_hour,work_day)
        st.write('the fare amount Predictis ', output)
if __name__=='__main__':
    main()

