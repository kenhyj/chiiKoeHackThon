import React, { useState } from "react";

import IconButton from '@mui/material/IconButton';

import StarTwoToneIcon from '@mui/icons-material/StarTwoTone';
import StarBorderTwoToneIcon from '@mui/icons-material/StarBorderTwoTone';
import StarIcon from '@mui/icons-material/Star';

import { grey } from '@mui/material/colors';

import Rating from '@mui/material/Rating';

import { styled } from '@mui/material/styles';

const StyledRating = styled(Rating)({
    '& .MuiRating-iconFilled': {
      color: "black",
    },
    '& .MuiRating-iconHover': {
      color: grey[500],
    },
  });


import { MuiThemeProvider, createTheme } from '@material-ui/core/styles';

const theme = createTheme({
    components: {
      // Name of the component
      MuiRating: {
        styleOverrides: {
          // Name of the slot
          iconFilled: {color: "green"},
          iconEmpty: {color: "white"},
        },
      },
    },
  });


export default function Stars(props) {
    const blackStar = [...Array(props.stars)].map((e, i) => <IconButton> <StarIcon style={{ color: "black" }} theme={theme} /> </IconButton>);
    const whiteStar = [...Array(5 - props.stars)].map((e, i) => <IconButton > <StarBorderTwoToneIcon /> </IconButton>);

    const greyStar = [...Array(props.stars)].map((e, i) => <IconButton> <StarIcon style={{color: grey[500] }} theme={theme}/> </IconButton>);

    // const oneLineStar = [...Array(5)].map((e, i) => props.stars > i ? <StarIcon />: <StarBorderTwoToneIcon/>);
    return (
        <div>
            <StyledRating
                value={props.stars}
                precision={0.5}
            />
            {/*
            {blackStar}
            {whiteStar} */}
        </div>
    )
}
