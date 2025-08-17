# 17855100 - Well-Kept Cache

## Common Data

| Field            | Value                  |
|------------------|------------------------|
| Zone             | Yorcia Weald (ID: 263) |
| Block Size       | 100 bytes              |
| Total Events     | 4                      |
| References Count | 3                      |

## List of Events

| Event ID                 | Entrypoint   |   Size |   Instructions |
|--------------------------|--------------|--------|----------------|
| [65535](#event-65535)    | 0x0000       |      1 |              1 |
| [128](#event-128)        | 0x0001       |      1 |              1 |
| [65535.1](#event-655351) | 0x0002       |     41 |             11 |
| [65535.2](#event-655352) | 0x002B       |     10 |              4 |

## DAT References (imed_data)

|   Index | Hex Value   |   Dec Value |
|---------|-------------|-------------|
|       0 | 0x012C      |         300 |
|       1 | 0x0000      |           0 |
|       2 | 0x0005      |           5 |

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

### Event 128

#### Metadata

| Field        | Value   |
|--------------|---------|
| Entrypoint   | 0x0001  |
| Data Size    | 1 bytes |
| Instructions | 1       |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0000:    00                                              .              
```

#### Opcodes

```
  0: 0x0001 [0x00] END_REQSTACK()
```

### Event 65535.1

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x0002   |
| Data Size    | 41 bytes |
| Instructions | 11       |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0000:       03 00 00 00 80 B4  0A 00 00 03 20 10 00 00    .......... ...
0010: 02 20 10 01 80 02 22 00  B4 0C 20 10 1C 02 80 01  . ...."... .....
0020: 10 00 B4 0B 05 21 10 B4  06 00 00                 .....!.....     
```

#### Opcodes

```
  0: 0x0002 [0x03] ExtData[1]->WorkLocal[0] = 300*
  1: 0x0007 [0xB4] UI_WINDOW_STRING_HANDLER(case=0x0A - Open event time window, work_offset=ExtData[1]->WorkLocal[0])
  2: 0x000B [0x03] Work_Zone[32] = ExtData[1]->WorkLocal[0]
  3: 0x0010 [0x02] IF !(Work_Zone[32] <= 0*) GOTO 0x0022
  4: 0x0018 [0xB4] UI_WINDOW_STRING_HANDLER(case=0x0C - Get event time count value, work_offset=Work_Zone[32])
  5: 0x001C [0x1C] WAIT(5* ticks)
  6: 0x001F [0x01] GOTO 0x0010
  7: 0x0022 [0xB4] UI_WINDOW_STRING_HANDLER(case=0x0B - Destroy event time window)
  8: 0x0024 [0x05] Work_Zone[33] = 1
  9: 0x0027 [0xB4] UI_WINDOW_STRING_HANDLER(case=0x06 - Toggle query message flag, flag_value=0x00)
 10: 0x002A [0x00] END_REQSTACK()
```

### Event 65535.2

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x002B   |
| Data Size    | 10 bytes |
| Instructions | 4        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0020:                                   06 20 10 06 21             . ..!
0030: 10 B4 06 01 00                                    .....           
```

#### Opcodes

```
  0: 0x002B [0x06] Work_Zone[32] = 0
  1: 0x002E [0x06] Work_Zone[33] = 0
  2: 0x0031 [0xB4] UI_WINDOW_STRING_HANDLER(case=0x06 - Toggle query message flag, flag_value=0x01)
  3: 0x0034 [0x00] END_REQSTACK()
```
