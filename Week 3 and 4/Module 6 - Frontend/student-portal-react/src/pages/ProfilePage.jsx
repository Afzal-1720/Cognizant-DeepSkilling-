import { useSelector, useDispatch } from "react-redux";

import { unenroll } from "../redux/enrollmentSlice";

function ProfilePage() {

    const dispatch = useDispatch();

    const enrolledCourses = useSelector(

        state => state.enrollment.enrolledCourses

    );

    return (

        <div className="container">

            <h2>My Enrolled Courses</h2>

            {

                enrolledCourses.length === 0 ?

                    <p>No courses enrolled.</p>

                    :

                    enrolledCourses.map(course => (

                        <div

                            className="card"

                            key={course.id}

                        >

                            <h3>{course.name}</h3>

                            <p>{course.code}</p>

                            <button

                                onClick={() =>

                                    dispatch(

                                        unenroll(course.id)

                                    )

                                }

                            >

                                Remove

                            </button>

                        </div>

                    ))

            }

        </div>

    );

}

export default ProfilePage;