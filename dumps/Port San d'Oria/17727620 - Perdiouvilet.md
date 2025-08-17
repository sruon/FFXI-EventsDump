# 17727620 - Perdiouvilet

## Common Data

| Field            | Value                     |
|------------------|---------------------------|
| Zone             | Port San d'Oria (ID: 232) |
| Block Size       | 280 bytes                 |
| Total Events     | 5                         |
| References Count | 19                        |

## List of Events

| Event ID              | Entrypoint   |   Size |   Instructions |
|-----------------------|--------------|--------|----------------|
| [65535](#event-65535) | 0x0000       |      1 |              1 |
| [762](#event-762)     | 0x0001       |     89 |             26 |
| [750](#event-750)     | 0x005A       |     74 |             16 |
| [792](#event-792)     | 0x00A4       |      1 |              1 |
| [793](#event-793)     | 0x00A5       |      1 |              1 |

## DAT References (imed_data)

|   Index | Hex Value   |   Dec Value |
|---------|-------------|-------------|
|       0 | 0x0001      |           1 |
|       1 | 0x2146      |        8518 |
|       2 | 0x2147      |        8519 |
|       3 | 0x0002      |           2 |
|       4 | 0x2148      |        8520 |
|       5 | 0x40000000  |  1073741824 |
|       6 | 0x0008      |           8 |
|       7 | 0x000F      |          15 |
|       8 | 0x214B      |        8523 |
|       9 | 0x214A      |        8522 |
|      10 | 0x2149      |        8521 |
|      11 | 0x21F2      |        8690 |
|      12 | 0x001E      |          30 |
|      13 | 0x2201      |        8705 |
|      14 | 0x0014      |          20 |
|      15 | 0x2202      |        8706 |
|      16 | 0x003C      |          60 |
|      17 | 0x0015      |          21 |
|      18 | 0x2203      |        8707 |

## String References

- **8518**: Greetings! Please excuse me...<chomp>... I'm just...<crunch>...eating lunch...<gulp>...
- **8519**: It can be fun to dine in fine company, but there are times when you simply want to eat alone.
- **8520**: Have you come for a meal, as well? You have a friend along, but my guess is that you'd prefer to eat by yourself.
- **8521**: Hmmm. Eating alone is actually rather dull. Why don't you share this with your partner? I seem to have lost my appetite.
- **8522**: What a great sense of partnership between you and %0! Your next meal is on me!
- **8523**: I had planned on devouring the entire menu of this establishment singlehandedly, but it appears my ambition lost out to indigestion. Perhaps you and %0 would care for one of these dishes?
- **8690**: <Player>'s badge flashes brightly.
- **8705**: I wonder what culinary delights grace the tables of the Near East.
- **8706**: The rice dish "pilaf" is rumored to be delicious. All those exotic spices...
- **8707**: <Rumble...> Oh! It seems I have awoken the beast of my appetite with all these gastronomic musings!

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

### Event 762

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x0001   |
| Data Size    | 89 bytes |
| Instructions | 18       |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0000:    1E F0 FF FF 7F 02 03  10 00 80 00 36 00 1D 01   ...........6...
0010: 80 23 02 08 10 00 80 00  21 00 1D 02 80 23 01 2D  .#......!....#.-
0020: 00 02 08 10 03 80 00 2D  00 1D 04 80 23 03 01 10  .......-....#...
0030: 05 80 21 01 59 00 02 07  10 06 80 04 54 00 02 07  ..!.Y.......T...
0040: 10 07 80 04 4D 00 1D 08  80 23 01 51 00 1D 09 80  ....M....#.Q....
0050: 23 01 58 00 1D 0A 80 23  21 00                    #.X....#!.      
```

#### Opcodes

```
  0: 0x0001 [0x1E] EventEntity looks at LocalPlayer and starts talking
  1: 0x0006 [0x02] IF !(Work_Zone[3] == 1*) GOTO 0x0036
  2: 0x000E [0x1D] PRINT_EVENT_MESSAGE(message_id=8518*)
    → "Greetings! Please excuse me...<chomp>... I'm just...<crunch>...eating lunch...<gulp>..."
  3: 0x0011 [0x23] WAIT_FOR_DIALOG_INTERACTION
  4: 0x0012 [0x02] IF !(Work_Zone[8] == 1*) GOTO 0x0021
  5: 0x001A [0x1D] PRINT_EVENT_MESSAGE(message_id=8519*)
    → "It can be fun to dine in fine company, but there are times when you simply want to eat alone."
  6: 0x001D [0x23] WAIT_FOR_DIALOG_INTERACTION
  7: 0x001E [0x01] GOTO 0x002D
  8: 0x0021 [0x02] IF !(Work_Zone[8] == 2*) GOTO 0x002D
  9: 0x0029 [0x1D] PRINT_EVENT_MESSAGE(message_id=8520*)
    → "Have you come for a meal, as well? You have a friend along, but my guess is that you'd prefer to eat by yourself."
 10: 0x002C [0x23] WAIT_FOR_DIALOG_INTERACTION

SUBROUTINE_002D:
 11: 0x002D [0x03] Work_Zone[1] = 1073741824*
 12: 0x0032 [0x21] END_EVENT

SUBROUTINE_0051:
 13: 0x0051 [0x01] GOTO 0x0058
 14: 0x0054 [0x1D] PRINT_EVENT_MESSAGE(message_id=8521*)
    → "Hmmm. Eating alone is actually rather dull. Why don't you share this with your partner? I seem to have lost my appetite."
 15: 0x0057 [0x23] WAIT_FOR_DIALOG_INTERACTION

SUBROUTINE_0058:
 16: 0x0058 [0x21] END_EVENT

SUBROUTINE_0059:
 17: 0x0059 [0x00] END_REQSTACK()
```

#### Data or dead code:

```
# Dead code (unreachable instructions):
     0x0033 [0x01] GOTO 0x0059
```

### Event 750

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x005A   |
| Data Size    | 74 bytes |
| Instructions | 16       |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0050:                                42 48 0B 80 1E F0            BH....
0060: FF FF 7F 1C 0C 80 1D 0D  80 23 66 0E 80 F8 FF FF  .........#f.....
0070: 7F F8 FF FF 7F 74 6C 6B  30 1D 0F 80 23 66 0E 80  .....tlk0...#f..
0080: F8 FF FF 7F F8 FF FF 7F  74 6C 6B 31 1C 10 80 66  ........tlk1...f
0090: 11 80 F8 FF FF 7F F8 FF  FF 7F 64 69 73 30 1D 12  ..........dis0..
00A0: 80 23 21 00                                       .#!.            
```

#### Opcodes

```
  0: 0x005A [0x42] SET_CLI_EVENT_CANCEL_DATA()
  1: 0x005B [0x48] [System] [8690*]:
    → "<Player>'s badge flashes brightly."
  2: 0x005E [0x1E] EventEntity looks at LocalPlayer and starts talking
  3: 0x0063 [0x1C] WAIT(30* ticks)
  4: 0x0066 [0x1D] PRINT_EVENT_MESSAGE(message_id=8705*)
    → "I wonder what culinary delights grace the tables of the Near East."
  5: 0x0069 [0x23] WAIT_FOR_DIALOG_INTERACTION
  6: 0x006A [0x66] LOAD_EXT_SCHEDULER_MAIN: Load scheduler "tlk0" with entities [EventEntity, EventEntity], work=20*
  7: 0x0079 [0x1D] PRINT_EVENT_MESSAGE(message_id=8706*)
    → "The rice dish "pilaf" is rumored to be delicious. All those exotic spices..."
  8: 0x007C [0x23] WAIT_FOR_DIALOG_INTERACTION
  9: 0x007D [0x66] LOAD_EXT_SCHEDULER_MAIN: Load scheduler "tlk1" with entities [EventEntity, EventEntity], work=20*
 10: 0x008C [0x1C] WAIT(60* ticks)
 11: 0x008F [0x66] LOAD_EXT_SCHEDULER_MAIN: Load scheduler "dis0" with entities [EventEntity, EventEntity], work=21*
 12: 0x009E [0x1D] PRINT_EVENT_MESSAGE(message_id=8707*)
    → "<Rumble...> Oh! It seems I have awoken the beast of my appetite with all these gastronomic musings!"
 13: 0x00A1 [0x23] WAIT_FOR_DIALOG_INTERACTION
 14: 0x00A2 [0x21] END_EVENT
 15: 0x00A3 [0x00] END_REQSTACK()
```

### Event 792

#### Metadata

| Field        | Value   |
|--------------|---------|
| Entrypoint   | 0x00A4  |
| Data Size    | 1 bytes |
| Instructions | 1       |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
00A0:             00                                        .           
```

#### Opcodes

```
  0: 0x00A4 [0x00] END_REQSTACK()
```

### Event 793

#### Metadata

| Field        | Value   |
|--------------|---------|
| Entrypoint   | 0x00A5  |
| Data Size    | 1 bytes |
| Instructions | 1       |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
00A0:                00                                      .          
```

#### Opcodes

```
  0: 0x00A5 [0x00] END_REQSTACK()
```
