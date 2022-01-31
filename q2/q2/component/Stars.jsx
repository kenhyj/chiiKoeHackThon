import React, { useState } from "react";

import IconButton from '@mui/material/IconButton';

import StarTwoToneIcon from '@mui/icons-material/StarTwoTone';
import StarBorderTwoToneIcon from '@mui/icons-material/StarBorderTwoTone';
import StarIcon from '@mui/icons-material/Star';
import styles from "./Stars.module.css";
import { grey } from '@mui/material/colors';

import Rating from '@mui/material/Rating';


import { MuiThemeProvider, createTheme } from '@material-ui/core/styles';

const theme = createTheme({
    overrides: {
        MuiIconButton: {
            root: {
                '&:hover': {
                    backgroundColor: "$labelcolor"
                }
            }
        }
    }
})


export default function Stars(props) {
    const blackStar = [...Array(props.stars)].map((e, i) => <IconButton> <StarIcon style={{ color: "black" }} theme={theme} /> </IconButton>);
    const whiteStar = [...Array(5 - props.stars)].map((e, i) => <IconButton > <StarBorderTwoToneIcon /> </IconButton>);

    // const greyStar = [...Array(props.stars)].map((e, i) => <IconButton> <StarIcon style={{color: grey[500] }} theme={theme}/> </IconButton>);

    // const oneLineStar = [...Array(5)].map((e, i) => props.stars > i ? <StarIcon />: <StarBorderTwoToneIcon/>);
    return (
        <div>
            <Rating
                value={props.stars}
                precision={0.5}
                iconFilled= {{color: "black"}}
            />
            {/*
            {blackStar}
            {whiteStar} */}
        </div>
        // <StarTwoToneIcon />
    )
}
