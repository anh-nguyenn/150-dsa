A state machine describes a system that is always in one of a few modes, with moves between modes triggered by events. Dynamic programming over those modes records the best value achievable in each mode after each event.

### Everyday examples

- **A parking meter.** You can be parked and holding a spot, walking away just after paying, or barred from parking for one interval because of a rule. Your best outcome after each hour depends on which mode you were in.
- **Freelance contracts.** You accept a contract, finish it and get paid, then must wait out a notice period before accepting another. Choosing when to start and finish contracts maximizes income.
- **Equipment rental.** A tool can be rented, returned for a refund, or unavailable for one day while it is being serviced. The best cash position each day is tracked per mode rather than per individual rental.

### How it shows up here

After each day the trader is either holding a share, has just sold and must rest tomorrow, or is free to buy. Each day's best balances come from the previous day's three modes, and the final answer is the best balance while not holding a share.
