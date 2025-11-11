# 17719640 - AMAN Reclaimer

## Common Data

| Field            | Value                         |
|------------------|-------------------------------|
| Zone             | Southern San d'Oria (ID: 230) |
| Block Size       | 244 bytes                     |
| Total Events     | 3                             |
| References Count | 13                            |

## List of Events

| Event ID              | Entrypoint   |   Size |   Instructions |
|-----------------------|--------------|--------|----------------|
| [65535](#event-65535) | 0x0000       |      1 |              1 |
| [3545](#event-3545)   | 0x0001       |     52 |             16 |
| [3546](#event-3546)   | 0x0035       |    109 |             30 |

## DAT References (imed_data)

|   Index | Hex Value   |   Dec Value |
|---------|-------------|-------------|
|       0 | 0x03E8      |        1000 |
|       1 | 0x2207      |        8711 |
|       2 | 0x3C66      |       15462 |
|       3 | 0x3C67      |       15463 |
|       4 | 0x3C68      |       15464 |
|       5 | 0x3C69      |       15465 |
|       6 | 0x3C6A      |       15466 |
|       7 | 0x3C6B      |       15467 |
|       8 | 0x0001      |           1 |
|       9 | 0x0000      |           0 |
|      10 | 0x3C6C      |       15468 |
|      11 | 0x3C6D      |       15469 |
|      12 | 0xFFFFFFF6  |  4294967286 |

## String References

- **15462**: The A.M.A.N. is pleased to announce a new service in which we purchase any equipment you no longer need--new or used.
- **15463**: Just trade me any piece of equipment you desire. I will quickly assess its value and award you with an appropriate number of reclamation marks.
- **15464**: Once you accumulate $0 of these marks, they will be automatically converted to one $1 and added to the total number held.
- **15465**: Though I am only authorized to accept a limited selection of equipment at present, the A.M.A.N. is considering making further additions to this list, so please check back regularly.
- **15466**: Would you like $0 reclamation mark[/s] in exchange for one $1? You currently have $5 mark[/s].
- **15467**: Proceed with the exchange? [Yes./No.]
- **15468**: The reclaimer awards you with $0 reclamation mark[/s] for a total of $2.
- **15469**: The reclaimer awards you with $0 reclamation mark[/s] for a total of $2. The number of $1 stored has increased by $3.

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

### Event 3545

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x0001   |
| Data Size    | 52 bytes |
| Instructions | 16       |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0000:    4A F0 FF FF 7F F8 FF  FF 7F 4A F8 FF FF 7F F0   J........J.....
0010: FF FF 7F 6F 76 F8 FF FF  7F 03 02 10 00 80 03 03  ...ov...........
0020: 10 01 80 1D 02 80 23 1D  03 80 23 1D 04 80 23 1D  ......#...#...#.
0030: 05 80 23 21 00                                    ..#!.           
```

#### Opcodes

```
  0: 0x0001 [0x4A] LocalPlayer looks at EventEntity
  1: 0x000A [0x4A] EventEntity looks at LocalPlayer
  2: 0x0013 [0x6F] WAIT_FRAME_DELAY: Yield until WaitTime reaches zero
  3: 0x0014 [0x76] CHECK_ENTITY_RENDER_FLAGS: Wait until EventEntity Render.Flags0 and Render.Flags3 conditions are met
  4: 0x0019 [0x03] Work_Zone[2] = 1000*
  5: 0x001E [0x03] Work_Zone[3] = 8711*
  6: 0x0023 [0x1D] PRINT_EVENT_MESSAGE(message_id=15462*)
    → "The A.M.A.N. is pleased to announce a new service in which we purchase any equipment you no longer need--new or used."
  7: 0x0026 [0x23] WAIT_FOR_DIALOG_INTERACTION
  8: 0x0027 [0x1D] PRINT_EVENT_MESSAGE(message_id=15463*)
    → "Just trade me any piece of equipment you desire. I will quickly assess its value and award you with an appropriate number of reclamation marks."
  9: 0x002A [0x23] WAIT_FOR_DIALOG_INTERACTION
 10: 0x002B [0x1D] PRINT_EVENT_MESSAGE(message_id=15464*)
    → "Once you accumulate $0 of these marks, they will be automatically converted to one $1 and added to the total number held."
 11: 0x002E [0x23] WAIT_FOR_DIALOG_INTERACTION
 12: 0x002F [0x1D] PRINT_EVENT_MESSAGE(message_id=15465*)
    → "Though I am only authorized to accept a limited selection of equipment at present, the A.M.A.N. is considering making further additions to this list, so please check back regularly."
 13: 0x0032 [0x23] WAIT_FOR_DIALOG_INTERACTION
 14: 0x0033 [0x21] END_EVENT
 15: 0x0034 [0x00] END_REQSTACK()
```

### Event 3546

#### Metadata

| Field        | Value     |
|--------------|-----------|
| Entrypoint   | 0x0035    |
| Data Size    | 109 bytes |
| Instructions | 24        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0030:                42 03 03  00 05 10 03 02 00 06 10       B..........
0040: 4A F0 FF FF 7F F8 FF FF  7F 4A F8 FF FF 7F F0 FF  J........J......
0050: FF 7F 6F 76 F8 FF FF 7F  1D 06 80 23 24 07 80 08  ..ov.......#$...
0060: 80 09 80 25 02 00 10 09  80 00 8E 00 03 03 10 01  ...%............
0070: 80 02 03 00 09 80 00 80  00 48 0A 80 23 01 84 00  .........H..#...
0080: 48 0B 80 23 03 01 10 02  00 21 00 01 A0 00 02 00  H..#.....!......
0090: 10 08 80 00 A0 00 03 01  10 0C 80 21 00 01 A0 00  ...........!....
00A0: 21 00                                             !.              
```

#### Opcodes

```
  0: 0x0035 [0x42] SET_CLI_EVENT_CANCEL_DATA()
  1: 0x0036 [0x03] ExtData[1]->WorkLocal[3] = Work_Zone[5]
  2: 0x003B [0x03] ExtData[1]->WorkLocal[2] = Work_Zone[6]
  3: 0x0040 [0x4A] LocalPlayer looks at EventEntity
  4: 0x0049 [0x4A] EventEntity looks at LocalPlayer
  5: 0x0052 [0x6F] WAIT_FRAME_DELAY: Yield until WaitTime reaches zero
  6: 0x0053 [0x76] CHECK_ENTITY_RENDER_FLAGS: Wait until EventEntity Render.Flags0 and Render.Flags3 conditions are met
  7: 0x0058 [0x1D] PRINT_EVENT_MESSAGE(message_id=15466*)
    → "Would you like $0 reclamation mark[/s] in exchange for one $1? You currently have $5 mark[/s]."
  8: 0x005B [0x23] WAIT_FOR_DIALOG_INTERACTION
  9: 0x005C [0x24] CREATE_DIALOG(message_id=15467*, default_option=1*, option_flags=0*)
    → "Proceed with the exchange? [Yes./No.]"
 10: 0x0063 [0x25] WAIT_DIALOG_SELECT()
 11: 0x0064 [0x02] IF !(Work_Zone[0] == 0*) GOTO 0x008E
 12: 0x006C [0x03] Work_Zone[3] = 8711*
 13: 0x0071 [0x02] IF !(ExtData[1]->WorkLocal[3] == 0*) GOTO 0x0080
 14: 0x0079 [0x48] [System] [15468*]:
    → "The reclaimer awards you with $0 reclamation mark[/s] for a total of $2."
 15: 0x007C [0x23] WAIT_FOR_DIALOG_INTERACTION
 16: 0x007D [0x01] GOTO 0x0084
 17: 0x0080 [0x48] [System] [15469*]:
    → "The reclaimer awards you with $0 reclamation mark[/s] for a total of $2. The number of $1 stored has increased by $3."
 18: 0x0083 [0x23] WAIT_FOR_DIALOG_INTERACTION

SUBROUTINE_0084:
 19: 0x0084 [0x03] Work_Zone[1] = ExtData[1]->WorkLocal[2]
 20: 0x0089 [0x21] END_EVENT
 21: 0x008A [0x00] END_REQSTACK()

SUBROUTINE_00A0:
 22: 0x00A0 [0x21] END_EVENT
 23: 0x00A1 [0x00] END_REQSTACK()
```

#### Data or dead code:

```
# Dead code (unreachable instructions):
     0x008B [0x01] GOTO 0x00A0
     0x009D [0x01] GOTO 0x00A0
```
