# 17224291 - Treasure Coffer

## Common Data

| Field            | Value                        |
|------------------|------------------------------|
| Zone             | Pashhow Marshlands (ID: 109) |
| Block Size       | 136 bytes                    |
| Total Events     | 2                            |
| References Count | 6                            |

## List of Events

| Event ID              | Entrypoint   |   Size |   Instructions |
|-----------------------|--------------|--------|----------------|
| [65535](#event-65535) | 0x0000       |      1 |              1 |
| [2000](#event-2000)   | 0x0001       |     85 |             21 |

## DAT References (imed_data)

|   Index | Hex Value   |   Dec Value |
|---------|-------------|-------------|
|       0 | 0x003C      |          60 |
|       1 | 0x2179      |        8569 |
|       2 | 0x0000      |           0 |
|       3 | 0x2178      |        8568 |
|       4 | 0x0001      |           1 |
|       5 | 0x0002      |           2 |

## String References

- **8568**: Obtain this item? [Yes./No.]
- **8569**: Obtain this item?

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

### Event 2000

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x0001   |
| Data Size    | 85 bytes |
| Instructions | 21       |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0000:    03 00 00 02 10 03 01  00 03 10 03 02 00 04 10   ...............
0010: 03 03 00 05 10 20 01 1C  00 80 CC 01 00 00 01 00  ..... ..........
0020: 02 00 03 00 48 01 80 23  93 02 80 24 03 80 04 80  ....H..#...$....
0030: 02 80 25 02 00 10 02 80  00 43 00 03 01 10 04 80  ..%......C......
0040: 01 53 00 02 00 10 04 80  00 53 00 03 01 10 05 80  .S.......S......
0050: 01 53 00 42 21 00                                 .S.B!.          
```

#### Opcodes

```
  0: 0x0001 [0x03] ExtData[1]->WorkLocal[0] = Work_Zone[2]
  1: 0x0006 [0x03] ExtData[1]->WorkLocal[1] = Work_Zone[3]
  2: 0x000B [0x03] ExtData[1]->WorkLocal[2] = Work_Zone[4]
  3: 0x0010 [0x03] ExtData[1]->WorkLocal[3] = Work_Zone[5]
  4: 0x0015 [0x20] SET_CLI_EVENT_UC_FLAG: Lock player control
  5: 0x0017 [0x1C] WAIT(60* ticks)
  6: 0x001A [0xCC] ITEM_INFO_WINDOW_HANDLER(case=0x01 - Open item info window (with chase), check_value=ExtData[1]->WorkLocal[0], buffer1=ExtData[1]->WorkLocal[1], buffer2=ExtData[1]->WorkLocal[2], buffer3=ExtData[1]->WorkLocal[3])
  7: 0x0024 [0x48] [System] [8569*]:
    → "Obtain this item?"
  8: 0x0027 [0x23] WAIT_FOR_DIALOG_INTERACTION
  9: 0x0028 [0x93] DISPLAY_ITEM_INFO(item_id=0*)
 10: 0x002B [0x24] CREATE_DIALOG(message_id=8568*, default_option=1*, option_flags=0*)
    → "Obtain this item? [Yes./No.]"
 11: 0x0032 [0x25] WAIT_DIALOG_SELECT()
 12: 0x0033 [0x02] IF !(Work_Zone[0] == 0*) GOTO 0x0043
 13: 0x003B [0x03] Work_Zone[1] = 1*
 14: 0x0040 [0x01] GOTO 0x0053
 15: 0x0043 [0x02] IF !(Work_Zone[0] == 1*) GOTO 0x0053
 16: 0x004B [0x03] Work_Zone[1] = 2*
 17: 0x0050 [0x01] GOTO 0x0053

SUBROUTINE_0053:
 18: 0x0053 [0x42] SET_CLI_EVENT_CANCEL_DATA()
 19: 0x0054 [0x21] END_EVENT
 20: 0x0055 [0x00] END_REQSTACK()
```
