import "../css/appointment.css";
import logo from "../assets/logotype.svg"
import dayjs from "dayjs";
import {Calendar, dayjsLocalizer }from "react-big-calendar";
import "react-big-calendar/lib/css/react-big-calendar.css";
import { useState } from "react";

export const AppointmentPage = () => {
const [modal, setModal] = useState(false);

const events = [
    {
        start: dayjs("2024-12-23T10:00:00").toDate(),
        end: dayjs("2024-12-23T11:00:00").toDate(),
        title: "haircut con cesar"
    }
]

const handleSubmit = (e) => {
    e.preventDefault();
    setModal(true);
}

const localizer = dayjsLocalizer(dayjs);
    return (
        <>
            <div className="div-form-one"> <div className="div-form-two"> </div></div>
            <div className="div-form-three">
                <div className="div-logo">
                    <img src={logo} alt="logotype" className="logo"/>
                    <h1>Appointment Barber Shop</h1>
                </div>
                
                <form action="">
                    <label htmlFor="name">name</label>
                    <input type="text" placeholder="Name" name="name"/>
                    <label htmlFor="lastname">lastname</label>
                    <input type="text" placeholder="Lastname" name="lastname" />
                    <label htmlFor="email">email</label>
                    <input type="email" placeholder="Email" name="email"/>
                    <label htmlFor="phone">phone</label>
                    <input type="text" placeholder="Phone" name="phone" />
                    <label htmlFor="description">description</label>
                    <input type="text" placeholder="Description" name="description" />
                    <label htmlFor="barber">barber</label>
                    <select name="barber">
                        <option value="César">Cesar</option>
                        <option value="barber1">barber1</option>
                        <option value="barber2">barber2</option>
                    </select>
                    <button onSubmit={(e) => handleSubmit(e)} type="submit">Select Appointment</button>
                </form>
            </div>

            
                {!modal && <div className="div-calendar">   
                    <button onClick={() => setModal(true)} type="button" className="x-calendar">X</button>
                    <h3>Calendar</h3>
                    <Calendar events={events} onSelectSlot={(e) => console.log(e)} localizer={localizer} messages={{next: ">", previous: "<"}} views={["month", "day"]} selectable/>
                </div>}
            
            
        </>
    );
};
