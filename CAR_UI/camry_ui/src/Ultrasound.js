import { useEffect, useState } from "react";


const Ultrasound = () => {

const [FR,set_FR] = useState('off')





// useEffect(() => {

//     const interval = setInterval(() => {
//         console.log('This will run every second!');
//         fetch("http://localhost:5000/Ultrasound").then(
//             res => res.text()
//         ).then(
//             FR => {
//                 set_FR(FR)
    
    
//             }
//         )
        

//       }, 1000);

      

//     return () => clearInterval(interval);


// });















    return ( 
        <>
        <p style={{paddingTop: "10px"}}>FR: {FR}</p>
        <p>FRC: {FR}</p>
        <p>FLC: {FR}</p>
        <p>FL: {FR}</p>
        <p>-------------------------------------</p>
        <p>RR: {FR}</p>
        <p>RRC: {FR}</p>
        <p>RLC: {FR}</p>
        <p>RL: {FR}</p>
        
        
        
        
        
        
        </>


     );
}
 
export default Ultrasound;