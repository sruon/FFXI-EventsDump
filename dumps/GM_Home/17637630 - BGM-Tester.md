# 17637630 - BGM-Tester

## Common Data

| Field            | Value             |
|------------------|-------------------|
| Zone             | GM_Home (ID: 210) |
| Block Size       | 88 bytes          |
| Total Events     | 2                 |
| References Count | 3                 |

## List of Events

| Event ID              | Entrypoint   |   Size |   Instructions |
|-----------------------|--------------|--------|----------------|
| [65535](#event-65535) | 0x0000       |      1 |              1 |
| [194](#event-194)     | 0x0001       |     51 |             13 |

## DAT References (imed_data)

|   Index | Hex Value   |   Dec Value |
|---------|-------------|-------------|
|       0 | 0x0001      |           1 |
|       1 | 0x0000      |           0 |
|       2 | 0x2411      |        9233 |

## String References

- **9233**: BGMF$0

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

### Event 194

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x0001   |
| Data Size    | 51 bytes |
| Instructions | 13       |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0000:    03 00 00 00 80 02 00  00 01 80 02 32 00 71 10   ...........2.q.
0010: 00 80 71 11 02 10 02 02  10 01 80 02 2C 00 5C 00  ..q.........,.\.
0020: 02 10 5C 01 02 10 48 02  80 01 2F 00 0C 00 00 01  ..\...H.../.....
0030: 06 00 21 00                                       ..!.            
```

#### Opcodes

```
  0: 0x0001 [0x03] ExtData[1]->WorkLocal[0] = 1*
  1: 0x0006 [0x02] IF !(ExtData[1]->WorkLocal[0] <= 0*) GOTO 0x0032
  2: 0x000E [0x71] USER_INPUT_HANDLER: Open numerical input dialog (work=1*)
  3: 0x0012 [0x71] USER_INPUT_HANDLER: Process numerical input A (work=Work_Zone[2])
  4: 0x0016 [0x02] IF !(Work_Zone[2] <= 0*) GOTO 0x002C
  5: 0x001E [0x5C] MUSIC_CONTROL: Set Idle (Day) music to song Work_Zone[2]
  6: 0x0022 [0x5C] MUSIC_CONTROL: Set Idle (Night) music to song Work_Zone[2]
  7: 0x0026 [0x48] [System] [9233*]:
    → "BGMF$0"
  8: 0x0029 [0x01] GOTO 0x002F
  9: 0x002C [0x0C] ExtData[1]->WorkLocal[0]--

SUBROUTINE_002F:
 10: 0x002F [0x01] GOTO 0x0006
 11: 0x0032 [0x21] END_EVENT
 12: 0x0033 [0x00] END_REQSTACK()
```
