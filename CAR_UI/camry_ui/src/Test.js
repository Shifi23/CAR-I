import { useEffect, useState } from "react";

const Test = () => {
    // let engine_status = 'on';
    const [engine_status, set_engine_status] = useState('off');
    const [lights,setLights] = useState('off')






    const handleCLick = () => {
        // if (engine_status === 'off'){
        //     set_engine_status("on")
        // }else{
        //     set_engine_status("off")
        // };
        // console.log('hi');
        fetch("http://localhost:5000/members").then(
            res => res.text()
        ).then(
            engine_status => {
                set_engine_status(engine_status)
                // console.log(engine_status)

            }
        )
        
    }

    const handleCLick_l = () => {
        fetch("http://localhost:5000/lights").then(
            res => res.text()
        ).then(
            lights => {
                setLights(lights)
                // console.log(lights)

            }
        )


    }

    // useEffect (() => {
    //     fetch("http://localhost:5000/members").then(
    //         res => res.text()
    //     ).then(
    //         engine_status => {
    //             set_engine_status(engine_status)
    //             // console.log(engine_status)

    //         }
    //     )
    //     fetch("http://localhost:5000/lights").then(
    //         res => res.text()
    //     ).then(
    //         lights => {
    //             setLights(lights)
    //             // console.log(lights)

    //         }
    //     )



    // },[])


    return ( 
        <div>
        <h1>This is a test page</h1>
        <div className="btn-group">
        <button onClick={handleCLick}>Engine {engine_status}</button>

        <button onClick={handleCLick}>Stop Engine</button>
        <button onClick={handleCLick}>Unlock Doors</button>
        <button onClick={handleCLick}>Lock Doors</button>
        <button onClick={handleCLick_l}>Lights {lights}</button>
        </div>
        <div className="container">
        <div className="row">
        <div className="column">
            <img src={"http://localhost:5000/camera"} alt="front" width="100%"/>
            </div>
            <div className="column">
            <img src={"http://localhost:5000/camera1"} alt="front" width="100%"/>
          </div>
        </div>
        </div>
        </div>


     );
}
 
export default Test;