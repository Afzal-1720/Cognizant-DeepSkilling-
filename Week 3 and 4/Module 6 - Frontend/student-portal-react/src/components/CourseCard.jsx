import { Link, useNavigate } from "react-router-dom";

import { useDispatch } from "react-redux";

import { enroll } from "../redux/enrollmentSlice";

function CourseCard({

    id,
    name,
    code,
    credits,
    grade

}) {

    const dispatch = useDispatch();

    const navigate = useNavigate();

    function handleEnroll() {

        dispatch(

            enroll({

                id,
                name,
                code,
                credits,
                grade

            })

        );

        navigate("/profile");

    }

    return (

        <div className="card">

            <h2>{name}</h2>

            <p>Code : {code}</p>

            <p>Credits : {credits}</p>

            <p>Grade : {grade}</p>

            <Link to={`/courses/${id}`}>

                View Details

            </Link>

            <br /><br />

            <button onClick={handleEnroll}>

                Enroll

            </button>

        </div>

    );

}

export default CourseCard;