# 17809503 - Marilleune

## Common Data

| Field            | Value          |
|------------------|----------------|
| Zone             | Norg (ID: 252) |
| Block Size       | 264 bytes      |
| Total Events     | 3              |
| References Count | 13             |

## List of Events

| Event ID              | Entrypoint   |   Size |   Instructions |
|-----------------------|--------------|--------|----------------|
| [65535](#event-65535) | 0x0000       |      1 |              1 |
| [131](#event-131)     | 0x0001       |    166 |             33 |
| [132](#event-132)     | 0x00A7       |     16 |              6 |

## DAT References (imed_data)

|   Index | Hex Value   |   Dec Value |
|---------|-------------|-------------|
|       0 | 0xFFFFFFFF  |  4294967295 |
|       1 | 0x00C8      |         200 |
|       2 | 0x0000      |           0 |
|       3 | 0x00C9      |         201 |
|       4 | 0x008A      |         138 |
|       5 | 0x296B      |       10603 |
|       6 | 0x2976      |       10614 |
|       7 | 0x2977      |       10615 |
|       8 | 0x296E      |       10606 |
|       9 | 0x0001      |           1 |
|      10 | 0x296F      |       10607 |
|      11 | 0x40000000  |  1073741824 |
|      12 | 0x296A      |       10602 |

## String References

- **10602**: If you wish to ride a chocobo, you must possess $6 and have a high enough job level.
- **10603**: You can rent a chocobo for $0 gil. I see you currently have $1 gil.
- **10606**: Do you wish to rent a chocobo? [Yes, I do./No, thank you.]
- **10607**: You don't have enough gil.
- **10614**: Our chocobos do not like traveling in the Sea Serpent Grotto, so we have dug a special exit tunnel leading from here to the Yuhtunga Jungle.
- **10615**: However, take care, as you will not be able to use this tunnel if you wish to return to Norg.

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

### Event 131

#### Metadata

| Field        | Value     |
|--------------|-----------|
| Entrypoint   | 0x0001    |
| Data Size    | 166 bytes |
| Instructions | 31        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0000:    02 02 10 00 80 00 36  00 42 45 01 80 F8 FF FF   ......6.BE.....
0010: 7F F8 FF FF 7F 66 64 6F  31 02 80 02 04 10 02 80  .....fdo1.......
0020: 00 34 00 45 03 80 F8 FF  FF 7F F8 FF FF 7F 63 68  .4.E..........ch
0030: 63 6F 02 80 21 00 03 09  10 04 80 1E F0 FF FF 7F  co..!...........
0040: 1D 05 80 23 1D 06 80 23  1D 07 80 23 24 08 80 09  ...#...#...#$...
0050: 80 02 80 25 02 00 10 02  80 00 A0 00 02 03 10 02  ...%............
0060: 10 04 92 00 42 45 01 80  F8 FF FF 7F F8 FF FF 7F  ....BE..........
0070: 66 64 6F 31 02 80 02 04  10 02 80 00 8F 00 45 03  fdo1..........E.
0080: 80 F8 FF FF 7F F8 FF FF  7F 63 68 63 6F 02 80 01  .........chco...
0090: 9B 00 1D 0A 80 23 03 01  10 0B 80 21 00 01 A5 00  .....#.....!....
00A0: 03 01 10 0B 80 21 00                              .....!.         
```

#### Opcodes

```
  0: 0x0001 [0x02] IF !(Work_Zone[2] == 4294967295*) GOTO 0x0036
  1: 0x0009 [0x42] SET_CLI_EVENT_CANCEL_DATA()
  2: 0x000A [0x45] LOAD_SCHEDULED_TASK: Load scheduler "fdo1" with entities [EventEntity, EventEntity], work=[200*, 0*]
  3: 0x001B [0x02] IF !(Work_Zone[4] == 0*) GOTO 0x0034
  4: 0x0023 [0x45] LOAD_SCHEDULED_TASK: Load scheduler "chco" with entities [EventEntity, EventEntity], work=[201*, 0*]
  5: 0x0034 [0x21] END_EVENT
  6: 0x0035 [0x00] END_REQSTACK()
  7: 0x0036 [0x03] Work_Zone[9] = 138*
  8: 0x003B [0x1E] EventEntity looks at LocalPlayer and starts talking
  9: 0x0040 [0x1D] PRINT_EVENT_MESSAGE(message_id=10603*)
    → "You can rent a chocobo for $0 gil. I see you currently have $1 gil."
 10: 0x0043 [0x23] WAIT_FOR_DIALOG_INTERACTION
 11: 0x0044 [0x1D] PRINT_EVENT_MESSAGE(message_id=10614*)
    → "Our chocobos do not like traveling in the Sea Serpent Grotto, so we have dug a special exit tunnel leading from here to the Yuhtunga Jungle."
 12: 0x0047 [0x23] WAIT_FOR_DIALOG_INTERACTION
 13: 0x0048 [0x1D] PRINT_EVENT_MESSAGE(message_id=10615*)
    → "However, take care, as you will not be able to use this tunnel if you wish to return to Norg."
 14: 0x004B [0x23] WAIT_FOR_DIALOG_INTERACTION
 15: 0x004C [0x24] CREATE_DIALOG(message_id=10606*, default_option=1*, option_flags=0*)
    → "Do you wish to rent a chocobo? [Yes, I do./No, thank you.]"
 16: 0x0053 [0x25] WAIT_DIALOG_SELECT()
 17: 0x0054 [0x02] IF !(Work_Zone[0] == 0*) GOTO 0x00A0
 18: 0x005C [0x02] IF !(Work_Zone[3] < Work_Zone[2]) GOTO 0x0092
 19: 0x0064 [0x42] SET_CLI_EVENT_CANCEL_DATA()
 20: 0x0065 [0x45] LOAD_SCHEDULED_TASK: Load scheduler "fdo1" with entities [EventEntity, EventEntity], work=[200*, 0*]
 21: 0x0076 [0x02] IF !(Work_Zone[4] == 0*) GOTO 0x008F
 22: 0x007E [0x45] LOAD_SCHEDULED_TASK: Load scheduler "chco" with entities [EventEntity, EventEntity], work=[201*, 0*]
 23: 0x008F [0x01] GOTO 0x009B
 24: 0x0092 [0x1D] PRINT_EVENT_MESSAGE(message_id=10607*)
    → "You don't have enough gil."
 25: 0x0095 [0x23] WAIT_FOR_DIALOG_INTERACTION
 26: 0x0096 [0x03] Work_Zone[1] = 1073741824*

SUBROUTINE_009B:
 27: 0x009B [0x21] END_EVENT
 28: 0x009C [0x00] END_REQSTACK()

SUBROUTINE_00A5:
 29: 0x00A5 [0x21] END_EVENT
 30: 0x00A6 [0x00] END_REQSTACK()
```

#### Data or dead code:

```
# Dead code (unreachable instructions):
     0x009D [0x01] GOTO 0x00A5
```

### Event 132

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x00A7   |
| Data Size    | 16 bytes |
| Instructions | 6        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
00A0:                      03  09 10 04 80 1E F0 FF FF         .........
00B0: 7F 1D 0C 80 23 21 00                              ....#!.         
```

#### Opcodes

```
  0: 0x00A7 [0x03] Work_Zone[9] = 138*
  1: 0x00AC [0x1E] EventEntity looks at LocalPlayer and starts talking
  2: 0x00B1 [0x1D] PRINT_EVENT_MESSAGE(message_id=10602*)
    → "If you wish to ride a chocobo, you must possess $6 and have a high enough job level."
  3: 0x00B4 [0x23] WAIT_FOR_DIALOG_INTERACTION
  4: 0x00B5 [0x21] END_EVENT
  5: 0x00B6 [0x00] END_REQSTACK()
```
