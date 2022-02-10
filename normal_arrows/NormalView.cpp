/*!
@file		NormalView.cpp

@brief		NormalView class.
@author		Teppei Kurita
@date		2016-06-27

Copyright 2016 Sony Corporation
*/

#include <iostream>
#include <opencv2/core/ocl.hpp>
#include "NormalView.h"


namespace polar{

NormalView::NormalView(void)
{
	width = 0;
	height = 0;
}

NormalView::~NormalView(void)
{
}

int NormalView::run(const cv::UMat& img, const cv::UMat& normal, const cv::Rect rect, const int step, const int power, const int radius, const int ambiInv)
{
	if(img.channels() !=3){
		std::cout << "Failed : unexpected number of channnels.";
	}

	if(img.cols != normal.cols || img.rows != normal.rows){
		std::cout << "Failed : Img size and Normal size must be equal";
	}

	//! initialize
	if(width!=img.cols || height!=img.rows){
		width  = img.cols;
		height = img.rows;
	}

	cv::Mat ref = normal.getMat(cv::ACCESS_READ).clone();
	if(ref.type() != CV_16UC3) normal.convertTo(ref, CV_16UC3, 256.0); 

	cv::Mat fref;
	ref.convertTo(fref, CV_32FC3, 1 / 65535.0);

	const float cnt = 0.5;

	cv::Mat out = img.getMat(cv::ACCESS_READ).clone();

	for(int y = rect.y ; y < rect.y + rect.height ; y += step){
		if( y > height - 1 ) continue;
		for(int x = rect.x ; x < rect.x + rect.width ; x += step){
			if( x > width - 1 ) continue;

			cv::Vec3f v = fref.at<cv::Vec3f>(y, x);

			v[1] = cnt - v[1];
			v[2] = v[2] - cnt;

			if(ambiInv){
				v[1] = -v[1];
				v[2] = -v[2];
			}

			int ex = static_cast<int>(x + v[2] * power);
			int ey = static_cast<int>(y + v[1] * power);

			ex = std::min(std::max(0, ex), width - 1);
			ey = std::min(std::max(0, ey), height - 1);

			cv::line(out, cv::Point(x, y), cv::Point(ex, ey), cv::Scalar(0, 0, 200 * 256), 1, CV_AA );
			cv::circle(out, cv::Point(ex, ey), radius, cv::Scalar(0, 0, 200 * 256), -1, CV_AA );
		
		}
	}

	viewImg = out.getUMat(cv::ACCESS_READ).clone();

	return 0;
}


}



