import React, { useState } from "react";
import StarTwoToneIcon from '@mui/icons-material/StarTwoTone';
import StarBorderTwoToneIcon from '@mui/icons-material/StarBorderTwoTone';
import StarIcon from '@mui/icons-material/Star';

export default function Stars(props) {

    for (const i = 0; i < props.stars; i++) {

    }
    for (const j = 0; j < 5 - props.stars; j++) {

    }

    const blackStar = [...Array(props.stars)].map((e, i) => <StarIcon />);
    const whiteStar = [...Array(5 - props.stars)].map((e, i) => <StarBorderTwoToneIcon />);
    return (
        <div>
            {blackStar}
            {whiteStar}
        </div>
        // <StarTwoToneIcon />
    )
}
