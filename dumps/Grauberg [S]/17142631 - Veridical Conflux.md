# 17142631 - Veridical Conflux

## Common Data

| Field            | Value                 |
|------------------|-----------------------|
| Zone             | Grauberg [S] (ID: 89) |
| Block Size       | 180 bytes             |
| Total Events     | 13                    |
| References Count | 6                     |

## List of Events

| Event ID              | Entrypoint   |   Size |   Instructions |
|-----------------------|--------------|--------|----------------|
| [65535](#event-65535) | 0x0000       |      1 |              1 |
| [28](#event-28)       | 0x0001       |      7 |              2 |
| [26](#event-26)       | 0x0008       |      9 |              3 |
| [29](#event-29)       | 0x0011       |     59 |             13 |
| [34](#event-34)       | 0x004C       |      1 |              1 |
| [40](#event-40)       | 0x004D       |      1 |              1 |
| [35](#event-35)       | 0x004E       |      1 |              1 |
| [41](#event-41)       | 0x004F       |      1 |              1 |
| [42](#event-42)       | 0x0050       |      1 |              1 |
| [43](#event-43)       | 0x0051       |      1 |              1 |
| [44](#event-44)       | 0x0052       |      1 |              1 |
| [45](#event-45)       | 0x0053       |      1 |              1 |
| [46](#event-46)       | 0x0054       |      1 |              1 |

## DAT References (imed_data)

|   Index | Hex Value   |   Dec Value |
|---------|-------------|-------------|
|       0 | 0x20BC      |        8380 |
|       1 | 0x0000      |           0 |
|       2 | 0x004F      |          79 |
|       3 | 0x0096      |         150 |
|       4 | 0x0028      |          40 |
|       5 | 0x0063      |          99 |

## String References

- **8380**: Warp to the Walk of Echoes? [Proceed./Not yet.]

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

### Event 28

#### Metadata

| Field        | Value   |
|--------------|---------|
| Entrypoint   | 0x0001  |
| Data Size    | 7 bytes |
| Instructions | 2       |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0000:    92 01 F8 FF FF 7F 00                            .......        
```

#### Opcodes

```
  0: 0x0001 [0x92] EventEntity->Render.Flags3 ^= 0x01
  1: 0x0007 [0x00] END_REQSTACK()
```

### Event 26

#### Metadata

| Field        | Value   |
|--------------|---------|
| Entrypoint   | 0x0008  |
| Data Size    | 9 bytes |
| Instructions | 3       |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0000:                          92 01 F8 FF FF 7F 22 01          ......".
0010: 00                                                .               
```

#### Opcodes

```
  0: 0x0008 [0x92] EventEntity->Render.Flags3 ^= 0x01
  1: 0x000E [0x22] ENTITY_HIDE_FLAG(enabled=0x01)
  2: 0x0010 [0x00] END_REQSTACK()
```

### Event 29

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x0011   |
| Data Size    | 59 bytes |
| Instructions | 13       |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0010:    42 06 01 10 24 00 80  01 80 01 80 25 02 00 10   B...$......%...
0020: 01 80 00 4A 00 CD 02 80  F0 FF FF 7F F0 FF FF 7F  ...J............
0030: 6D 61 69 6E 01 80 1C 03  80 92 01 F0 FF FF 7F 1C  main............
0040: 04 80 03 01 10 05 80 01  4A 00 21 00              ........J.!.    
```

#### Opcodes

```
  0: 0x0011 [0x42] SET_CLI_EVENT_CANCEL_DATA()
  1: 0x0012 [0x06] Work_Zone[1] = 0
  2: 0x0015 [0x24] CREATE_DIALOG(message_id=8380*, default_option=0*, option_flags=0*)
    → "Warp to the Walk of Echoes? [Proceed./Not yet.]"
  3: 0x001C [0x25] WAIT_DIALOG_SELECT()
  4: 0x001D [0x02] IF !(Work_Zone[0] == 0*) GOTO 0x004A
  5: 0x0025 [0xCD] LOAD_SCHEDULED_TASK_ALT4: Load scheduler "main" with entities [LocalPlayer, LocalPlayer], work=[79*, 0*]
  6: 0x0036 [0x1C] WAIT(150* ticks)
  7: 0x0039 [0x92] LocalPlayer->Render.Flags3 ^= 0x01
  8: 0x003F [0x1C] WAIT(40* ticks)
  9: 0x0042 [0x03] Work_Zone[1] = 99*
 10: 0x0047 [0x01] GOTO 0x004A

SUBROUTINE_004A:
 11: 0x004A [0x21] END_EVENT
 12: 0x004B [0x00] END_REQSTACK()
```

### Event 34

#### Metadata

| Field        | Value   |
|--------------|---------|
| Entrypoint   | 0x004C  |
| Data Size    | 1 bytes |
| Instructions | 1       |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0040:                                      00                       .   
```

#### Opcodes

```
  0: 0x004C [0x00] END_REQSTACK()
```

### Event 40

#### Metadata

| Field        | Value   |
|--------------|---------|
| Entrypoint   | 0x004D  |
| Data Size    | 1 bytes |
| Instructions | 1       |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0040:                                         00                     .  
```

#### Opcodes

```
  0: 0x004D [0x00] END_REQSTACK()
```

### Event 35

#### Metadata

| Field        | Value   |
|--------------|---------|
| Entrypoint   | 0x004E  |
| Data Size    | 1 bytes |
| Instructions | 1       |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0040:                                            00                   . 
```

#### Opcodes

```
  0: 0x004E [0x00] END_REQSTACK()
```

### Event 41

#### Metadata

| Field        | Value   |
|--------------|---------|
| Entrypoint   | 0x004F  |
| Data Size    | 1 bytes |
| Instructions | 1       |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0040:                                               00                 .
```

#### Opcodes

```
  0: 0x004F [0x00] END_REQSTACK()
```

### Event 42

#### Metadata

| Field        | Value   |
|--------------|---------|
| Entrypoint   | 0x0050  |
| Data Size    | 1 bytes |
| Instructions | 1       |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0050: 00                                                .               
```

#### Opcodes

```
  0: 0x0050 [0x00] END_REQSTACK()
```

### Event 43

#### Metadata

| Field        | Value   |
|--------------|---------|
| Entrypoint   | 0x0051  |
| Data Size    | 1 bytes |
| Instructions | 1       |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0050:    00                                              .              
```

#### Opcodes

```
  0: 0x0051 [0x00] END_REQSTACK()
```

### Event 44

#### Metadata

| Field        | Value   |
|--------------|---------|
| Entrypoint   | 0x0052  |
| Data Size    | 1 bytes |
| Instructions | 1       |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0050:       00                                            .             
```

#### Opcodes

```
  0: 0x0052 [0x00] END_REQSTACK()
```

### Event 45

#### Metadata

| Field        | Value   |
|--------------|---------|
| Entrypoint   | 0x0053  |
| Data Size    | 1 bytes |
| Instructions | 1       |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0050:          00                                          .            
```

#### Opcodes

```
  0: 0x0053 [0x00] END_REQSTACK()
```

### Event 46

#### Metadata

| Field        | Value   |
|--------------|---------|
| Entrypoint   | 0x0054  |
| Data Size    | 1 bytes |
| Instructions | 1       |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0050:             00                                        .           
```

#### Opcodes

```
  0: 0x0054 [0x00] END_REQSTACK()
```
