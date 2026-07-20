import { createContext, useState } from "react";

export const EnrollmentContext = createContext();

function EnrollmentProvider({ children }) {

    const [enrolledCourses, setEnrolledCourses] = useState([]);

    const enrollCourse = (course) => {

        const exists = enrolledCourses.find(
            c => c.id === course.id
        );

        if (!exists) {
            setEnrolledCourses([
                ...enrolledCourses,
                course
            ]);
        }
    };

    const removeCourse = (id) => {

        setEnrolledCourses(

            enrolledCourses.filter(

                course => course.id !== id

            )

        );

    };

    return (

        <EnrollmentContext.Provider
            value={{
                enrolledCourses,
                enrollCourse,
                removeCourse
            }}
        >

            {children}

        </EnrollmentContext.Provider>

    );

}

export default EnrollmentProvider;