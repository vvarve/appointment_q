import "../css/appointment.css";
import logo from "../assets/logotype.svg"
import { useState } from "react";
import { getDaysOFMonth, getHours, getMonthName, gettwentyfourHours, getYear, listNumberBefore } from "../resources/returns";
import { ViewHours } from "./ViewHours";

export const AppointmentPage = () => {
const [modal, setModal] = useState(false);
const [viewHour, setViewHour] = useState(false);
const [daySelect, setDaySelect] = useState(0);

const handleSubmit = () => {
    console.log("dayjs.month(11)")
    setModal(true);
    
}


    return (
        <>
            <div className="div-form-one">
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
                    <button onClick={() => setModal(true) & setViewHour(false)} type="button">Select Appointment</button>
                </form>
            </div>


            {modal &&<div className="div-calendar">
                <div className="div-calendar-header">
                    <h3>Calendar</h3>
                    <span onClick={() => setModal(false) & setViewHour(false)} className="close">x</span>
                </div>
                <div className="div-calendar-content">
                    <div className="div-arrow-month">
                        {viewHour && <span onClick={() => setViewHour(false)} className="span-arrow-back">&#11148;</span>}
                        <h3 className="h3-month">{getMonthName() + " " + getYear()}</h3>
                    </div>
                    {!viewHour && <div className="div-calendar-days">
                         <table>
                            <tbody>
                                <tr className="tr-day">
                                            <td></td>
                                {
                                    listNumberBefore(getDaysOFMonth()).map((item, index) => {
                                        return (
                                            
                                            <td onClick={() => setViewHour(true) & setDaySelect(item + 1)} key={index}>{item + 1}</td>
                                        )
                                    })
                                }
                                </tr>
                            </tbody>
                        </table>
                        
                    </div>}

                    {viewHour && <div className="div-calendar-hours">
                        <h3>Day {daySelect}</h3>
                         <ViewHours />
                    </div>}
                </div>
            </div>}
            
            
        </>
    );
};
