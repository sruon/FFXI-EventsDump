# 17363336 - Dock Lever

## Common Data

| Field            | Value                      |
|------------------|----------------------------|
| Zone             | Palborough Mines (ID: 143) |
| Block Size       | 188 bytes                  |
| Total Events     | 5                          |
| References Count | 8                          |

## List of Events

| Event ID              | Entrypoint   |   Size |   Instructions |
|-----------------------|--------------|--------|----------------|
| [65535](#event-65535) | 0x0000       |      1 |              1 |
| [14](#event-14)       | 0x0001       |     25 |              6 |
| [3](#event-3)         | 0x001A       |     77 |             13 |
| [6](#event-6)         | 0x0067       |      6 |              4 |
| [58](#event-58)       | 0x006D       |     11 |              7 |

## DAT References (imed_data)

|   Index | Hex Value   |   Dec Value |
|---------|-------------|-------------|
|       0 | 0x00C8      |         200 |
|       1 | 0x0000      |           0 |
|       2 | 0x0078      |         120 |
|       3 | 0x1CA2      |        7330 |
|       4 | 0x0001      |           1 |
|       5 | 0x1CA3      |        7331 |
|       6 | 0x0028      |          40 |
|       7 | 0x1CA4      |        7332 |

## String References

- **7330**: Pull lever? [Yes./No.]
- **7331**: The lever is stuck.
- **7332**: Nothing happens... Too many people on board?

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

### Event 14

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x0001   |
| Data Size    | 25 bytes |
| Instructions | 6        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0000:    42 45 00 80 F0 FF FF  7F F0 FF FF 7F 66 64 6F   BE..........fdo
0010: 32 01 80 1C 02 80 33 00  21 00                    2.....3.!.      
```

#### Opcodes

```
  0: 0x0001 [0x42] SET_CLI_EVENT_CANCEL_DATA()
  1: 0x0002 [0x45] LOAD_SCHEDULED_TASK: Load scheduler "fdo2" with entities [LocalPlayer, LocalPlayer], work=[200*, 0*]
  2: 0x0013 [0x1C] WAIT(120* ticks)
  3: 0x0016 [0x33] EventEntity->Render.Flags0 &= ~ 0x200000 // Bit 21 (flag=0x00)
  4: 0x0018 [0x21] END_EVENT
  5: 0x0019 [0x00] END_REQSTACK()
```

### Event 3

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x001A   |
| Data Size    | 77 bytes |
| Instructions | 13       |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0010:                                53 F0 FF FF 7F F0            S.....
0020: FF FF 7F 72 65 73 30 53  F0 FF FF 7F F0 FF FF 7F  ...res0S........
0030: 72 65 73 32 4A F0 FF FF  7F 88 F1 08 01 24 03 80  res2J........$..
0040: 04 80 01 80 25 02 00 10  01 80 00 55 00 03 01 10  ....%......U....
0050: 04 80 01 65 00 02 00 10  04 80 00 65 00 03 01 10  ...e.......e....
0060: 01 80 01 65 00 21 00                              ...e.!.         
```

#### Opcodes

```
  0: 0x001A [0x53] WAIT_SCHEDULER_TASK: Wait for scheduler "res0" with entities [LocalPlayer, LocalPlayer]
  1: 0x0027 [0x53] WAIT_SCHEDULER_TASK: Wait for scheduler "res2" with entities [LocalPlayer, LocalPlayer]
  2: 0x0034 [0x4A] LocalPlayer looks at Dock Lever (ID: 17363336/0x0108F188)
  3: 0x003D [0x24] CREATE_DIALOG(message_id=7330*, default_option=1*, option_flags=0*)
    → "Pull lever? [Yes./No.]"
  4: 0x0044 [0x25] WAIT_DIALOG_SELECT()
  5: 0x0045 [0x02] IF !(Work_Zone[0] == 0*) GOTO 0x0055
  6: 0x004D [0x03] Work_Zone[1] = 1*
  7: 0x0052 [0x01] GOTO 0x0065
  8: 0x0055 [0x02] IF !(Work_Zone[0] == 1*) GOTO 0x0065
  9: 0x005D [0x03] Work_Zone[1] = 0*
 10: 0x0062 [0x01] GOTO 0x0065

SUBROUTINE_0065:
 11: 0x0065 [0x21] END_EVENT
 12: 0x0066 [0x00] END_REQSTACK()
```

### Event 6

#### Metadata

| Field        | Value   |
|--------------|---------|
| Entrypoint   | 0x0067  |
| Data Size    | 6 bytes |
| Instructions | 4       |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0060:                      48  05 80 23 21 00                  H..#!.   
```

#### Opcodes

```
  0: 0x0067 [0x48] [System] [7331*]:
    → "The lever is stuck."
  1: 0x006A [0x23] WAIT_FOR_DIALOG_INTERACTION
  2: 0x006B [0x21] END_EVENT
  3: 0x006C [0x00] END_REQSTACK()
```

### Event 58

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x006D   |
| Data Size    | 11 bytes |
| Instructions | 7        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0060:                                         4C 1C 06               L..
0070: 80 4D 48 07 80 23 21 00                           .MH..#!.        
```

#### Opcodes

```
  0: 0x006D [0x4C] EventEntity->StatusEvent = 8 // Open door
  1: 0x006E [0x1C] WAIT(40* ticks)
  2: 0x0071 [0x4D] EventEntity->StatusEvent = 9 // Close door
  3: 0x0072 [0x48] [System] [7332*]:
    → "Nothing happens... Too many people on board?"
  4: 0x0075 [0x23] WAIT_FOR_DIALOG_INTERACTION
  5: 0x0076 [0x21] END_EVENT
  6: 0x0077 [0x00] END_REQSTACK()
```
