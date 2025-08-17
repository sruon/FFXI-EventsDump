# 17670754 - Yachemidot

## Common Data

| Field            | Value                      |
|------------------|----------------------------|
| Zone             | Abyssea - Altepa (ID: 218) |
| Block Size       | 232 bytes                  |
| Total Events     | 5                          |
| References Count | 17                         |

## List of Events

| Event ID              | Entrypoint   |   Size |   Instructions |
|-----------------------|--------------|--------|----------------|
| [65535](#event-65535) | 0x0000       |      1 |              1 |
| [284](#event-284)     | 0x0001       |      6 |              4 |
| [291](#event-291)     | 0x0007       |     84 |             26 |
| [292](#event-292)     | 0x005B       |     11 |              5 |
| [293](#event-293)     | 0x0066       |     25 |             11 |

## DAT References (imed_data)

|   Index | Hex Value   |   Dec Value |
|---------|-------------|-------------|
|       0 | 0x1FEE      |        8174 |
|       1 | 0x0014      |          20 |
|       2 | 0x1FE9      |        8169 |
|       3 | 0x1FEA      |        8170 |
|       4 | 0x06E2      |        1762 |
|       5 | 0x1FEB      |        8171 |
|       6 | 0x1FEC      |        8172 |
|       7 | 0x1FED      |        8173 |
|       8 | 0x0000      |           0 |
|       9 | 0x1FEF      |        8175 |
|      10 | 0x0002      |           2 |
|      11 | 0x0001      |           1 |
|      12 | 0x1FF0      |        8176 |
|      13 | 0x003C      |          60 |
|      14 | 0x1FF1      |        8177 |
|      15 | 0x1FF2      |        8178 |
|      16 | 0x1FF3      |        8179 |

## String References

- **8169**: Who goes there...?
- **8170**: Ah, so you are <Player>. Welcome.
- **8171**: The $3 you seek is indeed here. But I fear it will not be hatching now...nor ever.
- **8172**: <Player>. This $3 must be returned to its rightful home--the place where it was meant to begin its life. Will you do this for me?
- **8173**: Return the egg? [I shall./I shall not.]
- **8174**: ...
- **8175**: Excellent... Now go.
- **8176**: That $3 must be returned to its rightful home. The place where it was meant to begin life...
- **8177**: You have done well. Take this. I have need for it no more.
- **8178**: Now be off, and forget all that has transpired here. Shine your light upon the future, and let the past rest in darkness.
- **8179**: I...thank you...<Player>.

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

### Event 284

#### Metadata

| Field        | Value   |
|--------------|---------|
| Entrypoint   | 0x0001  |
| Data Size    | 6 bytes |
| Instructions | 4       |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0000:    1D 00 80 23 21 00                               ...#!.         
```

#### Opcodes

```
  0: 0x0001 [0x1D] PRINT_EVENT_MESSAGE(message_id=8174*)
    → "..."
  1: 0x0004 [0x23] WAIT_FOR_DIALOG_INTERACTION
  2: 0x0005 [0x21] END_EVENT
  3: 0x0006 [0x00] END_REQSTACK()
```

### Event 291

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x0007   |
| Data Size    | 84 bytes |
| Instructions | 26       |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0000:                      1E  F0 FF FF 7F 1C 01 80 1D         .........
0010: 02 80 23 1D 03 80 23 03  02 10 04 80 1D 05 80 23  ..#...#........#
0020: 03 02 10 04 80 1D 06 80  23 24 07 80 08 80 08 80  ........#$......
0030: 25 02 00 10 08 80 00 45  00 1D 09 80 23 03 01 10  %......E....#...
0040: 0A 80 01 59 00 02 00 10  0B 80 00 59 00 1D 00 80  ...Y.......Y....
0050: 23 03 01 10 0B 80 01 59  00 21 00                 #......Y.!.     
```

#### Opcodes

```
  0: 0x0007 [0x1E] EventEntity looks at LocalPlayer and starts talking
  1: 0x000C [0x1C] WAIT(20* ticks)
  2: 0x000F [0x1D] PRINT_EVENT_MESSAGE(message_id=8169*)
    → "Who goes there...?"
  3: 0x0012 [0x23] WAIT_FOR_DIALOG_INTERACTION
  4: 0x0013 [0x1D] PRINT_EVENT_MESSAGE(message_id=8170*)
    → "Ah, so you are <Player>. Welcome."
  5: 0x0016 [0x23] WAIT_FOR_DIALOG_INTERACTION
  6: 0x0017 [0x03] Work_Zone[2] = 1762*
  7: 0x001C [0x1D] PRINT_EVENT_MESSAGE(message_id=8171*)
    → "The $3 you seek is indeed here. But I fear it will not be hatching now...nor ever."
  8: 0x001F [0x23] WAIT_FOR_DIALOG_INTERACTION
  9: 0x0020 [0x03] Work_Zone[2] = 1762*
 10: 0x0025 [0x1D] PRINT_EVENT_MESSAGE(message_id=8172*)
    → "<Player>. This $3 must be returned to its rightful home--the place where it was meant to begin its life. Will you do this for me?"
 11: 0x0028 [0x23] WAIT_FOR_DIALOG_INTERACTION
 12: 0x0029 [0x24] CREATE_DIALOG(message_id=8173*, default_option=0*, option_flags=0*)
    → "Return the egg? [I shall./I shall not.]"
 13: 0x0030 [0x25] WAIT_DIALOG_SELECT()
 14: 0x0031 [0x02] IF !(Work_Zone[0] == 0*) GOTO 0x0045
 15: 0x0039 [0x1D] PRINT_EVENT_MESSAGE(message_id=8175*)
    → "Excellent... Now go."
 16: 0x003C [0x23] WAIT_FOR_DIALOG_INTERACTION
 17: 0x003D [0x03] Work_Zone[1] = 2*
 18: 0x0042 [0x01] GOTO 0x0059
 19: 0x0045 [0x02] IF !(Work_Zone[0] == 1*) GOTO 0x0059
 20: 0x004D [0x1D] PRINT_EVENT_MESSAGE(message_id=8174*)
    → "..."
 21: 0x0050 [0x23] WAIT_FOR_DIALOG_INTERACTION
 22: 0x0051 [0x03] Work_Zone[1] = 1*
 23: 0x0056 [0x01] GOTO 0x0059

SUBROUTINE_0059:
 24: 0x0059 [0x21] END_EVENT
 25: 0x005A [0x00] END_REQSTACK()
```

### Event 292

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x005B   |
| Data Size    | 11 bytes |
| Instructions | 5        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0050:                                   03 02 10 04 80             .....
0060: 1D 0C 80 23 21 00                                 ...#!.          
```

#### Opcodes

```
  0: 0x005B [0x03] Work_Zone[2] = 1762*
  1: 0x0060 [0x1D] PRINT_EVENT_MESSAGE(message_id=8176*)
    → "That $3 must be returned to its rightful home. The place where it was meant to begin life..."
  2: 0x0063 [0x23] WAIT_FOR_DIALOG_INTERACTION
  3: 0x0064 [0x21] END_EVENT
  4: 0x0065 [0x00] END_REQSTACK()
```

### Event 293

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x0066   |
| Data Size    | 25 bytes |
| Instructions | 11       |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0060:                   1C 0D  80 1E F0 FF FF 7F 1C 01        ..........
0070: 80 1D 0E 80 23 1D 0F 80  23 1D 10 80 23 21 00     ....#...#...#!. 
```

#### Opcodes

```
  0: 0x0066 [0x1C] WAIT(60* ticks)
  1: 0x0069 [0x1E] EventEntity looks at LocalPlayer and starts talking
  2: 0x006E [0x1C] WAIT(20* ticks)
  3: 0x0071 [0x1D] PRINT_EVENT_MESSAGE(message_id=8177*)
    → "You have done well. Take this. I have need for it no more."
  4: 0x0074 [0x23] WAIT_FOR_DIALOG_INTERACTION
  5: 0x0075 [0x1D] PRINT_EVENT_MESSAGE(message_id=8178*)
    → "Now be off, and forget all that has transpired here. Shine your light upon the future, and let the past rest in darkness."
  6: 0x0078 [0x23] WAIT_FOR_DIALOG_INTERACTION
  7: 0x0079 [0x1D] PRINT_EVENT_MESSAGE(message_id=8179*)
    → "I...thank you...<Player>."
  8: 0x007C [0x23] WAIT_FOR_DIALOG_INTERACTION
  9: 0x007D [0x21] END_EVENT
 10: 0x007E [0x00] END_REQSTACK()
```
