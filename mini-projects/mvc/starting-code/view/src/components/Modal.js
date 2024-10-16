/**
 * Model.js, é usado para apresentar o componente exportado LogExpense.jscomo um modelo.
 */
import * as React from 'react';
import Backdrop from '@mui/material/Backdrop';
import Box from '@mui/material/Box';
import Modal from '@mui/material/Modal';
import Fade from '@mui/material/Fade';
import LogExpense from './LogExpense';

const style = {
  position: 'absolute',
  top: '50%',
  left: '50%',
  transform: 'translate(-50%, -50%)',
  width: 400,
  bgcolor: 'background.paper',
  border: '2px solid #000',
  boxShadow: 24,
  p: 4,
};

const TransitionModal = ({
  modal,
  handleClose,
  setExpenses,
  expenses,
  _id,
}) => (
  <div>
    <Modal
      aria-labelledby="transition-modal-title"
      aria-describedby="transition-modal-description"
      open={modal}
      onClose={handleClose}
      closeAfterTransition
      BackdropComponent={Backdrop}
      BackdropProps={{
        timeout: 500,
      }}
    >
      <Fade in={modal}>
        <Box sx={style}>
          <LogExpense
            expense={expenses}
            setExpenses={(expensesList) => setExpenses(expensesList)}
            handleClose={() => handleClose()}
            _id={_id}
          />
        </Box>
      </Fade>
    </Modal>
  </div>
);

export default TransitionModal;
