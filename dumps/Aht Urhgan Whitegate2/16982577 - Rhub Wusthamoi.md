# 16982577 - Rhub Wusthamoi

## Common Data

| Field            | Value                          |
|------------------|--------------------------------|
| Zone             | Aht Urhgan Whitegate2 (ID: 50) |
| Block Size       | 92 bytes                       |
| Total Events     | 3                              |
| References Count | 5                              |

## List of Events

| Event ID                 | Entrypoint   |   Size |   Instructions |
|--------------------------|--------------|--------|----------------|
| [65535](#event-65535)    | 0x0000       |      1 |              1 |
| [65535.1](#event-655351) | 0x0001       |     18 |              4 |
| [65535.2](#event-655352) | 0x0013       |     23 |              7 |

## DAT References (imed_data)

|   Index | Hex Value   |   Dec Value |
|---------|-------------|-------------|
|       0 | 0x000D      |          13 |
|       1 | 0x002D      |          45 |
|       2 | 0x13D3A     |       81210 |
|       3 | 0xFFFE1469  |  4294841449 |
|       4 | 0xFFFFE890  |  4294961296 |

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

### Event 65535.1

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x0001   |
| Data Size    | 18 bytes |
| Instructions | 4        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0000:    6E 31 22 03 01 00 80  99 31 22 03 01 99 31 22   n1".....1"...1"
0010: 03 01 00                                          ...             
```

#### Opcodes

```
  0: 0x0001 [0x6E] Rhub Wusthamoi (ID: 16982577/0x01032231) uses emote 13*
  1: 0x0008 [0x99] Wait for Rhub Wusthamoi (ID: 16982577/0x01032231) animation to complete
  2: 0x000D [0x99] Wait for Rhub Wusthamoi (ID: 16982577/0x01032231) animation to complete
  3: 0x0012 [0x00] END_REQSTACK()
```

### Event 65535.2

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x0013   |
| Data Size    | 23 bytes |
| Instructions | 7        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0010:          1C 01 80 32 00  80 1F 00 02 80 03 80 04     ...2.........
0020: 80 1F 01 6F 1E 5C 21 03  01 00                    ...o.\!...      
```

#### Opcodes

```
  0: 0x0013 [0x1C] WAIT(45* ticks)
  1: 0x0016 [0x32] ExtData[1]->MainSpeed = 13* * 0.1
  2: 0x0019 [0x1F] MOVE_ENTITY: EventEntity moves to X=81.210*, Z=-125.847*, Y=-6.000*
  3: 0x0021 [0x1F] MOVE_ENTITY: Update entity position (mode=1)
  4: 0x0023 [0x6F] WAIT_FRAME_DELAY: Yield until WaitTime reaches zero
  5: 0x0024 [0x1E] EventEntity looks at Fari-Wari (ID: 16982364/0x0103215C) and starts talking
  6: 0x0029 [0x00] END_REQSTACK()
```
