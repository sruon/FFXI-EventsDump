# 16982154 - Nadee Periyaha

## Common Data

| Field            | Value                         |
|------------------|-------------------------------|
| Zone             | Aht Urhgan Whitegate (ID: 50) |
| Block Size       | 196 bytes                     |
| Total Events     | 6                             |
| References Count | 13                            |

## List of Events

| Event ID                 | Entrypoint   |   Size |   Instructions |
|--------------------------|--------------|--------|----------------|
| [65535](#event-65535)    | 0x0000       |      1 |              1 |
| [90](#event-90)          | 0x0001       |     62 |             18 |
| [849](#event-849)        | 0x003F       |      1 |              1 |
| [65535.1](#event-655351) | 0x0040       |      4 |              2 |
| [851](#event-851)        | 0x0044       |     19 |              9 |
| [852](#event-852)        | 0x0057       |     15 |              7 |

## DAT References (imed_data)

|   Index | Hex Value   |   Dec Value |
|---------|-------------|-------------|
|       0 | 0x24B1      |        9393 |
|       1 | 0x0008      |           8 |
|       2 | 0x24B2      |        9394 |
|       3 | 0x24B3      |        9395 |
|       4 | 0x24B4      |        9396 |
|       5 | 0x001E      |          30 |
|       6 | 0x24B5      |        9397 |
|       7 | 0x00B4      |         180 |
|       8 | 0x3159      |       12633 |
|       9 | 0x315A      |       12634 |
|      10 | 0x315B      |       12635 |
|      11 | 0x313C      |       12604 |
|      12 | 0x3187      |       12679 |

## String References

- **9393**: I'm Nadee Periyaha, the mercenary! I used to live in Nashmau.
- **9394**: Oh, don't tell me...you've met me there before?
- **9395**: I started to pick up Qiqirn ways when I was there. It can make life difficult, so you should be careful too!
- **9396**: There are many Qiqirn even in this town... Don't let your guard down, or yooo could end up speaking slooowly just like they dooo.
- **9397**: ...Oh no! I didn't do it again, did I!?
- **12604**: If you want to lure a Qiqirn out of hiding, you'll first need to learn how to talk like one.
- **12633**: I wonder what got into him?
- **12634**: Anyway, I think he may be able to shed a little light on our friend Kakkaroon's fear of children.
- **12635**: Why don't you go visit him at his shop?
- **12679**: Remember, "When in Rolanberry, one must eat the rolanberries."

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

### Event 90

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x0001   |
| Data Size    | 62 bytes |
| Instructions | 18       |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0000:    1E F0 FF FF 7F 6F 70  1D 00 80 23 66 01 80 F8   .....op...#f...
0010: FF FF 7F F8 FF FF 7F 61  77 77 30 1D 02 80 23 1D  .......aww0...#.
0020: 03 80 23 1D 04 80 23 66  01 80 F8 FF FF 7F F8 FF  ..#...#f........
0030: FF 7F 61 77 77 30 1C 05  80 1D 06 80 23 21 00     ..aww0......#!. 
```

#### Opcodes

```
  0: 0x0001 [0x1E] EventEntity looks at LocalPlayer and starts talking
  1: 0x0006 [0x6F] WAIT_FRAME_DELAY: Yield until WaitTime reaches zero
  2: 0x0007 [0x70] WAIT_ENTITY_RENDER_FLAG: Wait while EventEntity->Render.Flags3 bit 2 is set (cancel turn if not)
  3: 0x0008 [0x1D] PRINT_EVENT_MESSAGE(message_id=9393*)
    → "I'm Nadee Periyaha, the mercenary! I used to live in Nashmau."
  4: 0x000B [0x23] WAIT_FOR_DIALOG_INTERACTION
  5: 0x000C [0x66] LOAD_EXT_SCHEDULER_MAIN: Load scheduler "aww0" with entities [EventEntity, EventEntity], work=8*
  6: 0x001B [0x1D] PRINT_EVENT_MESSAGE(message_id=9394*)
    → "Oh, don't tell me...you've met me there before?"
  7: 0x001E [0x23] WAIT_FOR_DIALOG_INTERACTION
  8: 0x001F [0x1D] PRINT_EVENT_MESSAGE(message_id=9395*)
    → "I started to pick up Qiqirn ways when I was there. It can make life difficult, so you should be careful too!"
  9: 0x0022 [0x23] WAIT_FOR_DIALOG_INTERACTION
 10: 0x0023 [0x1D] PRINT_EVENT_MESSAGE(message_id=9396*)
    → "There are many Qiqirn even in this town... Don't let your guard down, or yooo could end up speaking slooowly just like they dooo."
 11: 0x0026 [0x23] WAIT_FOR_DIALOG_INTERACTION
 12: 0x0027 [0x66] LOAD_EXT_SCHEDULER_MAIN: Load scheduler "aww0" with entities [EventEntity, EventEntity], work=8*
 13: 0x0036 [0x1C] WAIT(30* ticks)
 14: 0x0039 [0x1D] PRINT_EVENT_MESSAGE(message_id=9397*)
    → "...Oh no! I didn't do it again, did I!?"
 15: 0x003C [0x23] WAIT_FOR_DIALOG_INTERACTION
 16: 0x003D [0x21] END_EVENT
 17: 0x003E [0x00] END_REQSTACK()
```

### Event 849

#### Metadata

| Field        | Value   |
|--------------|---------|
| Entrypoint   | 0x003F  |
| Data Size    | 1 bytes |
| Instructions | 1       |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0030:                                               00                 .
```

#### Opcodes

```
  0: 0x003F [0x00] END_REQSTACK()
```

### Event 65535.1

#### Metadata

| Field        | Value   |
|--------------|---------|
| Entrypoint   | 0x0040  |
| Data Size    | 4 bytes |
| Instructions | 2       |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0040: 1C 07 80 00                                       ....            
```

#### Opcodes

```
  0: 0x0040 [0x1C] WAIT(180* ticks)
  1: 0x0043 [0x00] END_REQSTACK()
```

### Event 851

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x0044   |
| Data Size    | 19 bytes |
| Instructions | 9        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0040:             1E F0 FF FF  7F 1D 08 80 23 1D 09 80      ........#...
0050: 23 1D 0A 80 23 21 00                              #...#!.         
```

#### Opcodes

```
  0: 0x0044 [0x1E] EventEntity looks at LocalPlayer and starts talking
  1: 0x0049 [0x1D] PRINT_EVENT_MESSAGE(message_id=12633*)
    → "I wonder what got into him?"
  2: 0x004C [0x23] WAIT_FOR_DIALOG_INTERACTION
  3: 0x004D [0x1D] PRINT_EVENT_MESSAGE(message_id=12634*)
    → "Anyway, I think he may be able to shed a little light on our friend Kakkaroon's fear of children."
  4: 0x0050 [0x23] WAIT_FOR_DIALOG_INTERACTION
  5: 0x0051 [0x1D] PRINT_EVENT_MESSAGE(message_id=12635*)
    → "Why don't you go visit him at his shop?"
  6: 0x0054 [0x23] WAIT_FOR_DIALOG_INTERACTION
  7: 0x0055 [0x21] END_EVENT
  8: 0x0056 [0x00] END_REQSTACK()
```

### Event 852

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x0057   |
| Data Size    | 15 bytes |
| Instructions | 7        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0050:                      1E  F0 FF FF 7F 1D 0B 80 23         ........#
0060: 1D 0C 80 23 21 00                                 ...#!.          
```

#### Opcodes

```
  0: 0x0057 [0x1E] EventEntity looks at LocalPlayer and starts talking
  1: 0x005C [0x1D] PRINT_EVENT_MESSAGE(message_id=12604*)
    → "If you want to lure a Qiqirn out of hiding, you'll first need to learn how to talk like one."
  2: 0x005F [0x23] WAIT_FOR_DIALOG_INTERACTION
  3: 0x0060 [0x1D] PRINT_EVENT_MESSAGE(message_id=12679*)
    → "Remember, "When in Rolanberry, one must eat the rolanberries.""
  4: 0x0063 [0x23] WAIT_FOR_DIALOG_INTERACTION
  5: 0x0064 [0x21] END_EVENT
  6: 0x0065 [0x00] END_REQSTACK()
```
