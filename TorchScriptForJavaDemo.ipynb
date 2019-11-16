{
 "cells": [
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "# Export a simple TorchScript model"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 1,
   "metadata": {},
   "outputs": [],
   "source": [
    "import torch"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 2,
   "metadata": {},
   "outputs": [],
   "source": [
    "class DemoModule(torch.nn.Module):\n",
    "    def forward(self, data, incr):\n",
    "        # type: (Tensor, float) -> Tensor\n",
    "        # Add the incr\n",
    "        larger = data + incr\n",
    "        # Then reduce sum over dim 0\n",
    "        thinner = torch.sum(larger, 0)\n",
    "        return thinner"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 3,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "DemoModule()"
      ]
     },
     "execution_count": 3,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "model = DemoModule()\n",
    "model.eval()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 4,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "RecursiveScriptModule(original_name=DemoModule)"
      ]
     },
     "execution_count": 4,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "smod = torch.jit.script(model)\n",
    "smod.eval()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 5,
   "metadata": {},
   "outputs": [],
   "source": [
    "smod.save(\"demo-model.pt1\")"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 6,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "RecursiveScriptModule(original_name=DemoModule)"
      ]
     },
     "execution_count": 6,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "loaded = torch.jit.load(\"demo-model.pt1\")\n",
    "loaded.eval()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 7,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "tensor([11., 13., 15.])"
      ]
     },
     "execution_count": 7,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "loaded(torch.tensor([[1,2,3],[4,5,6]]), 3.0)"
   ]
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "py3-pytorch-nightly",
   "language": "python",
   "name": "py3-pytorch-nightly"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.7.5"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 2
}
