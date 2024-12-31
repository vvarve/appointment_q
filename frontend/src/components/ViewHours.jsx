import { gettwentyfourHours } from "../resources/returns"

 
 export const ViewHours = () => {
    return (
        <table className="table-hour">
            <thead>
                <tr className="row-head-hour">
                    <th>Hour</th>
                    <th>Agend</th>
                </tr>
            </thead>
            <tbody>
                {gettwentyfourHours().map((hour) => {
                    return (
                        <tr >
                            <td className="hour" key={hour}>{hour}:00</td>
                            <td className="appointment">
                                <span className="hour-agend">Click here to register</span>
                            </td>
                        </tr>
                    )    
                })}
            </tbody>
        </table>
    )
}