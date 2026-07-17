function CourseCard({

    id,
    name,
    code,
    credits,
    grade,
    onEnroll

}) {

    return (

        <div className="card">

            <h2>{name}</h2>

            <p>Code : {code}</p>

            <p>Credits : {credits}</p>

            <p>Grade : {grade}</p>

            <button

                onClick={() =>
                    onEnroll({
                        id,
                        name,
                        code,
                        credits,
                        grade
                    })
                }

            >

                Enroll

            </button>

        </div>

    );

}

export default CourseCard;