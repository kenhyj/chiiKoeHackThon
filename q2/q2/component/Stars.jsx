import React, { useState } from "react";

import IconButton from '@mui/material/IconButton';

import StarTwoToneIcon from '@mui/icons-material/StarTwoTone';
import StarBorderTwoToneIcon from '@mui/icons-material/StarBorderTwoTone';
import StarIcon from '@mui/icons-material/Star';
import styles from "./Stars.module.css";

export default function Stars(props) {
    const blackStar = [...Array(props.stars)].map((e, i) => <IconButton > <StarIcon/> </IconButton>);
    const whiteStar = [...Array(5-props.stars)].map((e, i) => <IconButton > <StarBorderTwoToneIcon/> </IconButton>);

    // const oneLineStar = [...Array(5)].map((e, i) => props.stars > i ? <StarIcon />: <StarBorderTwoToneIcon/>);
    return (
        <div>
            {blackStar}
            {whiteStar}
        </div>
        // <StarTwoToneIcon />
    )
}
