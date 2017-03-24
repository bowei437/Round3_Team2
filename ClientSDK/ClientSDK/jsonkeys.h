#ifndef JSONKEYS_H
#define JSONKEYS_H

#include <QString>


// Boundary
const QString boundary_str = QString("boundary");
const QString boundary_info_str = QString("boundary_info");

//lat long
const QString latitude_str = QString("latitude");
const QString longitude_str = QString("longitude");

//goal
const QString goal_str = QString("goal");
const QString coordinates_str = QString("coordinates");

//obstacles
const QString obstacles_str = QString("obstacles");
const QString obstacle_id_str = QString("obstacle_id");
const QString obstacle_info_str = QString("obstacle_info");

//robots
const QString robot_str = QString("robot");
const QString robots_str = QString("robots");
const QString id_str = QString("id");

//robots
const QString path_str = QString("path");
//problem id
const QString problem_id_str = QString("problem_id");
const QString uid_str = QString("uid");

//version
const QString version_str = QString("version");

//shape
const QString shape_str = QString("shape");


#endif // JSONKEYS_H
