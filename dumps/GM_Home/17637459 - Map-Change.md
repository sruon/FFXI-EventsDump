# 17637459 - Map-Change

## Common Data

| Field            | Value             |
|------------------|-------------------|
| Zone             | GM_Home (ID: 210) |
| Block Size       | 128 bytes         |
| Total Events     | 2                 |
| References Count | 8                 |

## List of Events

| Event ID              | Entrypoint   |   Size |   Instructions |
|-----------------------|--------------|--------|----------------|
| [65535](#event-65535) | 0x0000       |      1 |              1 |
| [16](#event-16)       | 0x0001       |     68 |             17 |

## DAT References (imed_data)

|   Index | Hex Value   |   Dec Value |
|---------|-------------|-------------|
|       0 | 0x2360      |        9056 |
|       1 | 0x0000      |           0 |
|       2 | 0x0248      |         584 |
|       3 | 0x000C      |          12 |
|       4 | 0x0001      |           1 |
|       5 | 0x0251      |         593 |
|       6 | 0x0002      |           2 |
|       7 | 0x00D2      |         210 |

## String References

- **9056**: Change to what map? [Inside Adoulin Castle./Event-only Room./z210/Don't change!]

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

### Event 16

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x0001   |
| Data Size    | 68 bytes |
| Instructions | 17       |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0000:    24 00 80 01 80 01 80  25 02 00 10 01 80 00 1C   $......%.......
0010: 00 34 02 80 77 03 80 04  80 01 42 00 02 00 10 04  .4..w.....B.....
0020: 80 00 2F 00 34 05 80 77  03 80 04 80 01 42 00 02  ../.4..w.....B..
0030: 00 10 06 80 00 42 00 35  07 80 77 03 80 04 80 01  .....B.5..w.....
0040: 42 00 78 21 00                                    B.x!.           
```

#### Opcodes

```
  0: 0x0001 [0x24] CREATE_DIALOG(message_id=9056*, default_option=0*, option_flags=0*)
    → "Change to what map? [Inside Adoulin Castle./Event-only Room./z210/Don't change!]"
  1: 0x0008 [0x25] WAIT_DIALOG_SELECT()
  2: 0x0009 [0x02] IF !(Work_Zone[0] == 0*) GOTO 0x001C
  3: 0x0011 [0x34] LOAD_UNLOAD_ZONE(zone_id=584*)
  4: 0x0014 [0x77] SET_EVENT_TIME_WEATHER(hour=12*, weather=1*)
  5: 0x0019 [0x01] GOTO 0x0042
  6: 0x001C [0x02] IF !(Work_Zone[0] == 1*) GOTO 0x002F
  7: 0x0024 [0x34] LOAD_UNLOAD_ZONE(zone_id=593*)
  8: 0x0027 [0x77] SET_EVENT_TIME_WEATHER(hour=12*, weather=1*)
  9: 0x002C [0x01] GOTO 0x0042
 10: 0x002F [0x02] IF !(Work_Zone[0] == 2*) GOTO 0x0042
 11: 0x0037 [0x35] LOAD_ZONE_NO_CLOSE(zone_id=210*)
 12: 0x003A [0x77] SET_EVENT_TIME_WEATHER(hour=12*, weather=1*)
 13: 0x003F [0x01] GOTO 0x0042

SUBROUTINE_0042:
 14: 0x0042 [0x78] ENABLE_GAME_TIMER_RESET_WEATHER()
 15: 0x0043 [0x21] END_EVENT
 16: 0x0044 [0x00] END_REQSTACK()
```
