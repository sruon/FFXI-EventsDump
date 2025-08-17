# 17723552 - Secodiand

## Common Data

| Field            | Value                         |
|------------------|-------------------------------|
| Zone             | Northern San d'Oria (ID: 231) |
| Block Size       | 228 bytes                     |
| Total Events     | 4                             |
| References Count | 13                            |

## List of Events

| Event ID              | Entrypoint   |   Size |   Instructions |
|-----------------------|--------------|--------|----------------|
| [65535](#event-65535) | 0x0000       |     11 |              3 |
| [19](#event-19)       | 0x000B       |     84 |             27 |
| [17](#event-17)       | 0x005F       |     13 |              7 |
| [18](#event-18)       | 0x006C       |     33 |             10 |

## DAT References (imed_data)

|   Index | Hex Value   |   Dec Value |
|---------|-------------|-------------|
|       0 | 0x039A      |         922 |
|       1 | 0x0002      |           2 |
|       2 | 0x0000      |           0 |
|       3 | 0x2F40      |       12096 |
|       4 | 0x2F41      |       12097 |
|       5 | 0x2F43      |       12099 |
|       6 | 0x0001      |           1 |
|       7 | 0x2F44      |       12100 |
|       8 | 0x2F45      |       12101 |
|       9 | 0x2F42      |       12098 |
|      10 | 0x2F46      |       12102 |
|      11 | 0x2F47      |       12103 |
|      12 | 0x00C9      |         201 |

## String References

- **12096**: There's something foul in the air of late. Can you not feel it? I must get some charms to ward away this wickedness.
- **12097**: To make such charms I need $1 $0 ! Might you bring me some?
- **12098**: I need $1 more $0 ! Please, give me any you find!
- **12099**: How about it? [I'll do it./I'll pass.]
- **12100**: I am in your debt! I need them to ward away darkness, you know! Remember, that's $1 $0 !
- **12101**: Very well. But still the darkness draws closer... I must do something!
- **12102**: Remember, I need $1 $0 ! Make haste!
- **12103**: Thank you! This should hold the darkness at bay...if only for a while. Bring more, if you can.

## Events

### Event 65535

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x0000   |
| Data Size    | 11 bytes |
| Instructions | 3        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0000: 03 02 10 00 80 03 03 10  01 80 00                 ...........     
```

#### Opcodes

```
  0: 0x0000 [0x03] Work_Zone[2] = 922*
  1: 0x0005 [0x03] Work_Zone[3] = 2*
  2: 0x000A [0x00] END_REQSTACK()
```

### Event 19

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x000B   |
| Data Size    | 84 bytes |
| Instructions | 27       |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0000:                                   03 00 00 09 10             .....
0010: 06 01 10 1E F0 FF FF 7F  6F 70 02 00 00 02 80 00  ........op......
0020: 59 00 1D 03 80 23 1D 04  80 23 24 05 80 06 80 02  Y....#...#$.....
0030: 80 25 02 00 10 02 80 00  47 00 42 1D 07 80 23 03  .%......G.B...#.
0040: 01 10 06 80 01 56 00 02  00 10 06 80 00 56 00 1D  .....V.......V..
0050: 08 80 23 01 56 00 01 5D  00 1D 09 80 23 21 00     ..#.V..]....#!. 
```

#### Opcodes

```
  0: 0x000B [0x03] ExtData[1]->WorkLocal[0] = Work_Zone[9]
  1: 0x0010 [0x06] Work_Zone[1] = 0
  2: 0x0013 [0x1E] EventEntity looks at LocalPlayer and starts talking
  3: 0x0018 [0x6F] WAIT_FRAME_DELAY: Yield until WaitTime reaches zero
  4: 0x0019 [0x70] WAIT_ENTITY_RENDER_FLAG: Wait while EventEntity->Render.Flags3 bit 2 is set (cancel turn if not)
  5: 0x001A [0x02] IF !(ExtData[1]->WorkLocal[0] == 0*) GOTO 0x0059
  6: 0x0022 [0x1D] PRINT_EVENT_MESSAGE(message_id=12096*)
    → "There's something foul in the air of late. Can you not feel it? I must get some charms to ward away this wickedness."
  7: 0x0025 [0x23] WAIT_FOR_DIALOG_INTERACTION
  8: 0x0026 [0x1D] PRINT_EVENT_MESSAGE(message_id=12097*)
    → "To make such charms I need $1 $0 ! Might you bring me some?"
  9: 0x0029 [0x23] WAIT_FOR_DIALOG_INTERACTION
 10: 0x002A [0x24] CREATE_DIALOG(message_id=12099*, default_option=1*, option_flags=0*)
    → "How about it? [I'll do it./I'll pass.]"
 11: 0x0031 [0x25] WAIT_DIALOG_SELECT()
 12: 0x0032 [0x02] IF !(Work_Zone[0] == 0*) GOTO 0x0047
 13: 0x003A [0x42] SET_CLI_EVENT_CANCEL_DATA()
 14: 0x003B [0x1D] PRINT_EVENT_MESSAGE(message_id=12100*)
    → "I am in your debt! I need them to ward away darkness, you know! Remember, that's $1 $0 !"
 15: 0x003E [0x23] WAIT_FOR_DIALOG_INTERACTION
 16: 0x003F [0x03] Work_Zone[1] = 1*
 17: 0x0044 [0x01] GOTO 0x0056
 18: 0x0047 [0x02] IF !(Work_Zone[0] == 1*) GOTO 0x0056
 19: 0x004F [0x1D] PRINT_EVENT_MESSAGE(message_id=12101*)
    → "Very well. But still the darkness draws closer... I must do something!"
 20: 0x0052 [0x23] WAIT_FOR_DIALOG_INTERACTION
 21: 0x0053 [0x01] GOTO 0x0056

SUBROUTINE_0056:
 22: 0x0056 [0x01] GOTO 0x005D
 23: 0x0059 [0x1D] PRINT_EVENT_MESSAGE(message_id=12098*)
    → "I need $1 more $0 ! Please, give me any you find!"
 24: 0x005C [0x23] WAIT_FOR_DIALOG_INTERACTION

SUBROUTINE_005D:
 25: 0x005D [0x21] END_EVENT
 26: 0x005E [0x00] END_REQSTACK()
```

### Event 17

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x005F   |
| Data Size    | 13 bytes |
| Instructions | 7        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0050:                                               1E                 .
0060: F0 FF FF 7F 6F 70 1D 0A  80 23 21 00              ....op...#!.    
```

#### Opcodes

```
  0: 0x005F [0x1E] EventEntity looks at LocalPlayer and starts talking
  1: 0x0064 [0x6F] WAIT_FRAME_DELAY: Yield until WaitTime reaches zero
  2: 0x0065 [0x70] WAIT_ENTITY_RENDER_FLAG: Wait while EventEntity->Render.Flags3 bit 2 is set (cancel turn if not)
  3: 0x0066 [0x1D] PRINT_EVENT_MESSAGE(message_id=12102*)
    → "Remember, I need $1 $0 ! Make haste!"
  4: 0x0069 [0x23] WAIT_FOR_DIALOG_INTERACTION
  5: 0x006A [0x21] END_EVENT
  6: 0x006B [0x00] END_REQSTACK()
```

### Event 18

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x006C   |
| Data Size    | 33 bytes |
| Instructions | 10       |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0060:                                      20 01 42 1E               .B.
0070: F0 FF FF 7F 6F 70 1D 0B  80 23 45 0C 80 F0 FF FF  ....op...#E.....
0080: 7F F0 FF FF 7F 71 73 74  63 02 80 21 00           .....qstc..!.   
```

#### Opcodes

```
  0: 0x006C [0x20] SET_CLI_EVENT_UC_FLAG: Lock player control
  1: 0x006E [0x42] SET_CLI_EVENT_CANCEL_DATA()
  2: 0x006F [0x1E] EventEntity looks at LocalPlayer and starts talking
  3: 0x0074 [0x6F] WAIT_FRAME_DELAY: Yield until WaitTime reaches zero
  4: 0x0075 [0x70] WAIT_ENTITY_RENDER_FLAG: Wait while EventEntity->Render.Flags3 bit 2 is set (cancel turn if not)
  5: 0x0076 [0x1D] PRINT_EVENT_MESSAGE(message_id=12103*)
    → "Thank you! This should hold the darkness at bay...if only for a while. Bring more, if you can."
  6: 0x0079 [0x23] WAIT_FOR_DIALOG_INTERACTION
  7: 0x007A [0x45] LOAD_SCHEDULED_TASK: Load scheduler "qstc" with entities [LocalPlayer, LocalPlayer], work=[201*, 0*]
  8: 0x008B [0x21] END_EVENT
  9: 0x008C [0x00] END_REQSTACK()
```
