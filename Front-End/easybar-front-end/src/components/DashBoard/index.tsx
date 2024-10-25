import Despesas from "./despesas";
import { Despesas2 } from "./despesas2";

export default function FormDashBoard() {
    return (
        <>
            <div className="flex">
                <div className="w-2/3">
                    <Despesas />
                </div>
                <div className="w-1/3">
                    <Despesas2 />
                </div>
            </div>
            <div className="flex">
                <div className="w-1/3">
                    <Despesas2 />
                </div>
                <div className="w-2/3">
                    <Despesas />
                </div>
            </div>
        </>
    )
}
