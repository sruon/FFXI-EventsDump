# 17814128 - Romaa Mihgo

## Common Data

| Field            | Value                          |
|------------------|--------------------------------|
| Zone             | Abyssea - Uleguerand (ID: 253) |
| Block Size       | 248 bytes                      |
| Total Events     | 2                              |
| References Count | 17                             |

## List of Events

| Event ID              | Entrypoint   |   Size |   Instructions |
|-----------------------|--------------|--------|----------------|
| [65535](#event-65535) | 0x0000       |      1 |              1 |
| [356](#event-356)     | 0x0001       |    153 |             43 |

## DAT References (imed_data)

|   Index | Hex Value   |   Dec Value |
|---------|-------------|-------------|
|       0 | 0x0064      |         100 |
|       1 | 0x001A      |          26 |
|       2 | 0x1FC1      |        8129 |
|       3 | 0x1FC2      |        8130 |
|       4 | 0x004B      |          75 |
|       5 | 0x0020      |          32 |
|       6 | 0x1FBF      |        8127 |
|       7 | 0x1FC0      |        8128 |
|       8 | 0x0032      |          50 |
|       9 | 0x0007      |           7 |
|      10 | 0x1FBD      |        8125 |
|      11 | 0x1FBE      |        8126 |
|      12 | 0x0019      |          25 |
|      13 | 0x1FBB      |        8123 |
|      14 | 0x1FBC      |        8124 |
|      15 | 0x1FB9      |        8121 |
|      16 | 0x1FBA      |        8122 |

## String References

- **8121**: The fiends are strong, and numerous. I'll be frrrank with you--the odds are against us.
- **8122**: Grrr... It's just like it was in the Great War. But we were victorious then, and we can do it again!
- **8123**: We've put a dent in their rrranks, but they still outnumber us.
- **8124**: Do I need t' spell it out for you!? This is no time to be standing about. Get out there on the battlefield. We're fightin' for our futurrre here!
- **8125**: Finally, we've gained the upperrr hand.
- **8126**: But this is no time to rrrest on our laurels. Our job's not through until the last currrsed fiend has drawn its dyin' breath!
- **8127**: Can ya smell that in the air? That's the scent of our enemy's fear!
- **8128**: Victorrry is close at hand! We must strike like a cobra and sink our fangs deep into our foe's dark heart!
- **8129**: It's quiet here. Too quiet for my likin'...
- **8130**: We may have won the day, but we must rrremain ever vigilant. A desperate foe's a dangerrrous foe.

## Events

### Event 65535

#### Metadata

| Field        | Value   |
|--------------|---------|
| Entrypoint   | 0x0000  |
| Data Size    | 1 bytes |
| Instructions | 1       |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0000: 00                                                .               
```

#### Opcodes

```
  0: 0x0000 [0x00] END_REQSTACK()
```

### Event 356

#### Metadata

| Field        | Value     |
|--------------|-----------|
| Entrypoint   | 0x0001    |
| Data Size    | 153 bytes |
| Instructions | 43        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0000:    1E F0 FF FF 7F 6F 70  02 02 10 00 80 02 27 00   .....op......'.
0010: 6E 70 D2 0F 01 01 80 99  70 D2 0F 01 1D 02 80 23  np......p......#
0020: 1D 03 80 23 01 98 00 02  02 10 04 80 02 46 00 6E  ...#.........F.n
0030: 70 D2 0F 01 05 80 99 70  D2 0F 01 1D 06 80 23 1D  p......p......#.
0040: 07 80 23 01 98 00 02 02  10 08 80 02 65 00 6E 70  ..#.........e.np
0050: D2 0F 01 09 80 99 70 D2  0F 01 1D 0A 80 23 1D 0B  ......p......#..
0060: 80 23 01 98 00 02 02 10  0C 80 02 84 00 6E 70 D2  .#...........np.
0070: 0F 01 05 80 99 70 D2 0F  01 1D 0D 80 23 1D 0E 80  .....p......#...
0080: 23 01 98 00 6E 70 D2 0F  01 05 80 99 70 D2 0F 01  #...np......p...
0090: 1D 0F 80 23 1D 10 80 23  21 00                    ...#...#!.      
```

#### Opcodes

```
  0: 0x0001 [0x1E] EventEntity looks at LocalPlayer and starts talking
  1: 0x0006 [0x6F] WAIT_FRAME_DELAY: Yield until WaitTime reaches zero
  2: 0x0007 [0x70] WAIT_ENTITY_RENDER_FLAG: Wait while EventEntity->Render.Flags3 bit 2 is set (cancel turn if not)
  3: 0x0008 [0x02] IF !(Work_Zone[2] <= 100*) GOTO 0x0027
  4: 0x0010 [0x6E] Romaa Mihgo (ID: 17814128/0x010FD270) uses emote 26*
  5: 0x0017 [0x99] Wait for Romaa Mihgo (ID: 17814128/0x010FD270) animation to complete
  6: 0x001C [0x1D] PRINT_EVENT_MESSAGE(message_id=8129*)
    → "It's quiet here. Too quiet for my likin'..."
  7: 0x001F [0x23] WAIT_FOR_DIALOG_INTERACTION
  8: 0x0020 [0x1D] PRINT_EVENT_MESSAGE(message_id=8130*)
    → "We may have won the day, but we must rrremain ever vigilant. A desperate foe's a dangerrrous foe."
  9: 0x0023 [0x23] WAIT_FOR_DIALOG_INTERACTION
 10: 0x0024 [0x01] GOTO 0x0098
 11: 0x0027 [0x02] IF !(Work_Zone[2] <= 75*) GOTO 0x0046
 12: 0x002F [0x6E] Romaa Mihgo (ID: 17814128/0x010FD270) uses emote 32*
 13: 0x0036 [0x99] Wait for Romaa Mihgo (ID: 17814128/0x010FD270) animation to complete
 14: 0x003B [0x1D] PRINT_EVENT_MESSAGE(message_id=8127*)
    → "Can ya smell that in the air? That's the scent of our enemy's fear!"
 15: 0x003E [0x23] WAIT_FOR_DIALOG_INTERACTION
 16: 0x003F [0x1D] PRINT_EVENT_MESSAGE(message_id=8128*)
    → "Victorrry is close at hand! We must strike like a cobra and sink our fangs deep into our foe's dark heart!"
 17: 0x0042 [0x23] WAIT_FOR_DIALOG_INTERACTION
 18: 0x0043 [0x01] GOTO 0x0098
 19: 0x0046 [0x02] IF !(Work_Zone[2] <= 50*) GOTO 0x0065
 20: 0x004E [0x6E] Romaa Mihgo (ID: 17814128/0x010FD270) uses emote 7*
 21: 0x0055 [0x99] Wait for Romaa Mihgo (ID: 17814128/0x010FD270) animation to complete
 22: 0x005A [0x1D] PRINT_EVENT_MESSAGE(message_id=8125*)
    → "Finally, we've gained the upperrr hand."
 23: 0x005D [0x23] WAIT_FOR_DIALOG_INTERACTION
 24: 0x005E [0x1D] PRINT_EVENT_MESSAGE(message_id=8126*)
    → "But this is no time to rrrest on our laurels. Our job's not through until the last currrsed fiend has drawn its dyin' breath!"
 25: 0x0061 [0x23] WAIT_FOR_DIALOG_INTERACTION
 26: 0x0062 [0x01] GOTO 0x0098
 27: 0x0065 [0x02] IF !(Work_Zone[2] <= 25*) GOTO 0x0084
 28: 0x006D [0x6E] Romaa Mihgo (ID: 17814128/0x010FD270) uses emote 32*
 29: 0x0074 [0x99] Wait for Romaa Mihgo (ID: 17814128/0x010FD270) animation to complete
 30: 0x0079 [0x1D] PRINT_EVENT_MESSAGE(message_id=8123*)
    → "We've put a dent in their rrranks, but they still outnumber us."
 31: 0x007C [0x23] WAIT_FOR_DIALOG_INTERACTION
 32: 0x007D [0x1D] PRINT_EVENT_MESSAGE(message_id=8124*)
    → "Do I need t' spell it out for you!? This is no time to be standing about. Get out there on the battlefield. We're fightin' for our futurrre here!"
 33: 0x0080 [0x23] WAIT_FOR_DIALOG_INTERACTION
 34: 0x0081 [0x01] GOTO 0x0098
 35: 0x0084 [0x6E] Romaa Mihgo (ID: 17814128/0x010FD270) uses emote 32*
 36: 0x008B [0x99] Wait for Romaa Mihgo (ID: 17814128/0x010FD270) animation to complete
 37: 0x0090 [0x1D] PRINT_EVENT_MESSAGE(message_id=8121*)
    → "The fiends are strong, and numerous. I'll be frrrank with you--the odds are against us."
 38: 0x0093 [0x23] WAIT_FOR_DIALOG_INTERACTION
 39: 0x0094 [0x1D] PRINT_EVENT_MESSAGE(message_id=8122*)
    → "Grrr... It's just like it was in the Great War. But we were victorious then, and we can do it again!"
 40: 0x0097 [0x23] WAIT_FOR_DIALOG_INTERACTION

SUBROUTINE_0098:
 41: 0x0098 [0x21] END_EVENT
 42: 0x0099 [0x00] END_REQSTACK()
```
