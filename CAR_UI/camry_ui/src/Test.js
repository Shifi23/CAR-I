import { useState } from "react";
import Ultrasound from "./Ultrasound";




const Test = () => {
    // let engine_status = 'on';
    const [engine_status, set_engine_status] = useState('off');
    const [lights, setLights] = useState('off');
    const [door, setDoor] = useState("Locked");
    const [voltage, setVoltage] = useState('null')






    const handleCLick_EN = () => {

        fetch("http://localhost:5000/StartCar").then(
            res => res.text()
        ).then(
            engine_status => {
                set_engine_status(engine_status)

            }
        )

    }

    const handleCLick_ENS = () => {
        fetch("http://localhost:5000/StopCar").then(
            res => res.text()
        ).then(
            engine_status => {
                set_engine_status(engine_status)

            }
        )


    }

    const handleCLick_LI = () => {
        fetch("http://localhost:5000/lights").then(
            res => res.text()
        ).then(
            lights => {
                setLights(lights)


            }
        )


    }


    const handleCLick_UL = () => {
        fetch("http://localhost:5000/unlockCar").then(
            res => res.text()
        ).then(
            door => {
                setDoor(door)


            }
        )


    }

    const handleCLick_LOC = () => {
        fetch("http://localhost:5000/lockCar").then(
            res => res.text()
        ).then(
            door => {
                setDoor(door)


            }
        )


    }


    const handleCLick_VOL = () => {
        fetch("http://localhost:5000/Voltage").then(
            res => res.text()
        ).then(
            voltage => {
                setVoltage(voltage)


            }
        )


    }








    return (

        <>
            <h1 style={{ paddingBottom: "50px" }}>System Test-beta</h1>
            <div className="grid-container">
                <div className="grid-child">
                    <h3>Controls:</h3>
                    <div className="btn-group">
                        <button onClick={handleCLick_EN}>Start Engine</button>
                        <button onClick={handleCLick_ENS}>Stop Engine</button>
                        <button onClick={handleCLick_UL}>Unlock Doors</button>
                        <button onClick={handleCLick_LOC}>Lock Doors</button>
                        <button onClick={handleCLick_LI}>Parking Lights</button>
                    </div>

                    <h3 style={{ paddingTop: "40px" }}>Stats:</h3>
                    <p style={{ paddingTop: "10px" }}>Engine: {engine_status}</p>
                    <p>Parking Lights: {lights}</p>
                    <p style={{ paddingBottom: "10px" }} >Doors: {door}</p>
                    <div className="lockunlock">
                        <span className={door === "Unlocked" ? "lock unlocked" : "lock"}></span>
                    </div>
                </div>


                <div className="grid-child">
                    <h3>Camera's:</h3>
                    {/* <img src={"http://localhost:5000/camera"} alt='Front Camera' width={320} height={240} ></img> */}
                    {/* <img src={"http://localhost:5000/camera"} alt='Front Camera' width={320} height={240} ></img> */}



                </div>

                <div className="grid-child">
                    <h3>Proximity Sensor's:</h3>
                    <Ultrasound></Ultrasound>




                </div>
                <div className="grid-child">
                    <h3>OBD-II:</h3>
                    <p style={{ paddingTop: "10px" }} onClick={handleCLick_VOL}>Voltage: {voltage}</p>
                    <p> Speed: Igniton is off</p>
                    <p> RPM: Igniton is off</p>
                    <p> Engine Load: Igniton is off</p>
                    <p> Fuel: Igniton is off</p>


                </div>

            </div>


        </>




    );
}

export default Test;