import { useEffect, useState } from "react";


const Ultrasound = () => {

const [sensor_data,set_sensor_data] = useState({"front": [1, 2, 4, 5],
"rear": [1, 4, 6, 2]
})





useEffect(() => {

    const interval = setInterval(() => {
        console.log('This will run every second!');
        fetch("http://localhost:5000/Ultrasound").then(
            res => res.json()
        ).then(
            FR => 
                set_sensor_data(FR)
        )
        
      }, 3000);

      

    return () => clearInterval(interval);


});





    return ( 
        <>
        
        <p style={{paddingTop: "10px"}}>FR: {sensor_data.front[0]}</p>
        <p>FRC: {sensor_data.front[1]}</p>
        <p>FLC: {sensor_data.front[2]}</p>
        <p>FL: {sensor_data.front[3]}</p>
        <p>-------------------------------------</p>
        <p>RR: {sensor_data.rear[0]}</p>
        <p>RRC: {sensor_data.rear[1]}</p>
        <p>RLC: {sensor_data.rear[2]}</p>
        <p>RL: {sensor_data.rear[3]}</p>
        
        
        
        
        
        
        </>


     );
}
 
export default Ultrasound;




