import StarTwoToneIcon from '@mui/icons-material/StarBorderTwoTone';
import StarIcon from '@mui/icons-material/Star';
import { createMuiTheme, MuiThemeProvider } from '@material-ui/core';

const hoverTheme = createMuiTheme(
    {status: {
        hover: gray[300]
    }}
)
const clickTheme = createMuiTheme(
    {status: {
        click: gray[1000]
    }}
)
const defaultTheme =  createMuiTheme(
    {staus: {
        default: gray[0]
    }}
)

export default function FiveStars() {
    return (
        <div>
            <ThemeProvider theme={click} >
                <StarTwoToneIcon />
            </ThemeProvider>
            <StarTwoToneIcon />
            <StarTwoToneIcon />
            <StarTwoToneIcon />
            <StarIcon color={"primary"}/>
        </div>
    ) 
}
