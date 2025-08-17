# 17637390 - Party_test

## Common Data

| Field            | Value             |
|------------------|-------------------|
| Zone             | GM_Home (ID: 210) |
| Block Size       | 196 bytes         |
| Total Events     | 2                 |
| References Count | 9                 |

## List of Events

| Event ID              | Entrypoint   |   Size |   Instructions |
|-----------------------|--------------|--------|----------------|
| [65535](#event-65535) | 0x0000       |      1 |              1 |
| [25](#event-25)       | 0x0001       |    133 |             33 |

## DAT References (imed_data)

|   Index | Hex Value   |   Dec Value |
|---------|-------------|-------------|
|       0 | 0x000F      |          15 |
|       1 | 0x0001      |           1 |
|       2 | 0x0002      |           2 |
|       3 | 0x0003      |           3 |
|       4 | 0x1BC8      |        7112 |
|       5 | 0x0004      |           4 |
|       6 | 0x1BC9      |        7113 |
|       7 | 0x0005      |           5 |
|       8 | 0x1BCA      |        7114 |

## String References

- **7112**: $10$P11.$17*<Player>a$$3$2228778i<B
- **7113**: $m$P110*<Player>a$$3$2228778i<B
- **7114**: $3W$3 $3u*<Player>a$$3$2228778i<B

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

### Event 25

#### Metadata

| Field        | Value     |
|--------------|-----------|
| Entrypoint   | 0x0001    |
| Data Size    | 133 bytes |
| Instructions | 33        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0000:    06 01 10 42 1E F0 FF  FF 7F 1C 00 80 4A F0 FF   ...B........J..
0010: FF 7F F8 FF FF 7F 6F 76  F0 FF FF 7F 1A 21 00 21  ......ov.....!.!
0020: 00 43 00 43 01 03 00 00  02 10 02 00 00 01 80 80  .C.C............
0030: 35 00 01 85 00 02 00 00  02 80 80 40 00 01 85 00  5..........@....
0040: 02 00 00 03 80 80 57 00  02 01 00 01 80 00 54 00  ......W.......T.
0050: 1D 04 80 23 01 85 00 02  00 00 05 80 80 6E 00 02  ...#.........n..
0060: 01 00 02 80 00 6B 00 1D  06 80 23 01 85 00 02 00  .....k....#.....
0070: 00 07 80 80 85 00 02 01  00 03 80 00 82 00 1D 08  ................
0080: 80 23 01 85 00 1B                                 .#....          
```

#### Opcodes

```
  0: 0x0001 [0x06] Work_Zone[1] = 0
  1: 0x0004 [0x42] SET_CLI_EVENT_CANCEL_DATA()
  2: 0x0005 [0x1E] EventEntity looks at LocalPlayer and starts talking
  3: 0x000A [0x1C] WAIT(15* ticks)
  4: 0x000D [0x4A] LocalPlayer looks at EventEntity
  5: 0x0016 [0x6F] WAIT_FRAME_DELAY: Yield until WaitTime reaches zero
  6: 0x0017 [0x76] CHECK_ENTITY_RENDER_FLAGS: Wait until LocalPlayer Render.Flags0 and Render.Flags3 conditions are met
  7: 0x001C [0x1A] CALL_SUBROUTINE(address=0x0021)
  8: 0x001F [0x21] END_EVENT
  9: 0x0020 [0x00] END_REQSTACK()

SUBROUTINE_0021:
 10: 0x0021 [0x43] SEND_EVENT_UPDATE: Send pending tag to server (packet 0x005B)
 11: 0x0023 [0x43] SEND_EVENT_UPDATE: Check pending flag (skip if not pending)
 12: 0x0025 [0x03] ExtData[1]->WorkLocal[0] = Work_Zone[2]
 13: 0x002A [0x02] IF !(ExtData[1]->WorkLocal[0] == 1*) GOTO 0x0035
 14: 0x0032 [0x01] GOTO 0x0085
 15: 0x0035 [0x02] IF !(ExtData[1]->WorkLocal[0] == 2*) GOTO 0x0040
 16: 0x003D [0x01] GOTO 0x0085
 17: 0x0040 [0x02] IF !(ExtData[1]->WorkLocal[0] == 3*) GOTO 0x0057
 18: 0x0048 [0x02] IF !(ExtData[1]->WorkLocal[1] == 1*) GOTO 0x0054
 19: 0x0050 [0x1D] PRINT_EVENT_MESSAGE(message_id=7112*)
    → "$10$P11.$17*<Player>a$$3$2228778i<B"
 20: 0x0053 [0x23] WAIT_FOR_DIALOG_INTERACTION
 21: 0x0054 [0x01] GOTO 0x0085
 22: 0x0057 [0x02] IF !(ExtData[1]->WorkLocal[0] == 4*) GOTO 0x006E
 23: 0x005F [0x02] IF !(ExtData[1]->WorkLocal[1] == 2*) GOTO 0x006B
 24: 0x0067 [0x1D] PRINT_EVENT_MESSAGE(message_id=7113*)
    → "$m$P110*<Player>a$$3$2228778i<B"
 25: 0x006A [0x23] WAIT_FOR_DIALOG_INTERACTION
 26: 0x006B [0x01] GOTO 0x0085
 27: 0x006E [0x02] IF !(ExtData[1]->WorkLocal[0] == 5*) GOTO 0x0085
 28: 0x0076 [0x02] IF !(ExtData[1]->WorkLocal[1] == 3*) GOTO 0x0082
 29: 0x007E [0x1D] PRINT_EVENT_MESSAGE(message_id=7114*)
    → "$3W$3 $3u*<Player>a$$3$2228778i<B"
 30: 0x0081 [0x23] WAIT_FOR_DIALOG_INTERACTION
 31: 0x0082 [0x01] GOTO 0x0085

SUBROUTINE_0085:
 32: 0x0085 [0x1B] RETURN
```
