# 17523319 - Veridical Conflux

## Common Data

| Field            | Value                    |
|------------------|--------------------------|
| Zone             | Walk of Echoes (ID: 182) |
| Block Size       | 124 bytes                |
| Total Events     | 5                        |
| References Count | 6                        |

## List of Events

| Event ID              | Entrypoint   |   Size |   Instructions |
|-----------------------|--------------|--------|----------------|
| [65535](#event-65535) | 0x0000       |      1 |              1 |
| [3](#event-3)         | 0x0001       |     59 |             13 |
| [123](#event-123)     | 0x003C       |      1 |              1 |
| [26](#event-26)       | 0x003D       |      1 |              1 |
| [30](#event-30)       | 0x003E       |      1 |              1 |

## DAT References (imed_data)

|   Index | Hex Value   |   Dec Value |
|---------|-------------|-------------|
|       0 | 0x1E57      |        7767 |
|       1 | 0x0000      |           0 |
|       2 | 0x004F      |          79 |
|       3 | 0x0096      |         150 |
|       4 | 0x0028      |          40 |
|       5 | 0x0063      |          99 |

## String References

- **7767**: Warp to Witchfire Glen? [Proceed./Not now.]

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

### Event 3

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x0001   |
| Data Size    | 59 bytes |
| Instructions | 13       |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0000:    42 06 01 10 24 00 80  01 80 01 80 25 02 00 10   B...$......%...
0010: 01 80 00 3A 00 CD 02 80  F0 FF FF 7F F0 FF FF 7F  ...:............
0020: 6D 61 69 6E 01 80 1C 03  80 92 01 F0 FF FF 7F 1C  main............
0030: 04 80 03 01 10 05 80 01  3A 00 21 00              ........:.!.    
```

#### Opcodes

```
  0: 0x0001 [0x42] SET_CLI_EVENT_CANCEL_DATA()
  1: 0x0002 [0x06] Work_Zone[1] = 0
  2: 0x0005 [0x24] CREATE_DIALOG(message_id=7767*, default_option=0*, option_flags=0*)
    → "Warp to Witchfire Glen? [Proceed./Not now.]"
  3: 0x000C [0x25] WAIT_DIALOG_SELECT()
  4: 0x000D [0x02] IF !(Work_Zone[0] == 0*) GOTO 0x003A
  5: 0x0015 [0xCD] LOAD_SCHEDULED_TASK_ALT4: Load scheduler "main" with entities [LocalPlayer, LocalPlayer], work=[79*, 0*]
  6: 0x0026 [0x1C] WAIT(150* ticks)
  7: 0x0029 [0x92] LocalPlayer->Render.Flags3 ^= 0x01
  8: 0x002F [0x1C] WAIT(40* ticks)
  9: 0x0032 [0x03] Work_Zone[1] = 99*
 10: 0x0037 [0x01] GOTO 0x003A

SUBROUTINE_003A:
 11: 0x003A [0x21] END_EVENT
 12: 0x003B [0x00] END_REQSTACK()
```

### Event 123

#### Metadata

| Field        | Value   |
|--------------|---------|
| Entrypoint   | 0x003C  |
| Data Size    | 1 bytes |
| Instructions | 1       |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0030:                                      00                       .   
```

#### Opcodes

```
  0: 0x003C [0x00] END_REQSTACK()
```

### Event 26

#### Metadata

| Field        | Value   |
|--------------|---------|
| Entrypoint   | 0x003D  |
| Data Size    | 1 bytes |
| Instructions | 1       |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0030:                                         00                     .  
```

#### Opcodes

```
  0: 0x003D [0x00] END_REQSTACK()
```

### Event 30

#### Metadata

| Field        | Value   |
|--------------|---------|
| Entrypoint   | 0x003E  |
| Data Size    | 1 bytes |
| Instructions | 1       |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0030:                                            00                   . 
```

#### Opcodes

```
  0: 0x003E [0x00] END_REQSTACK()
```
